#!/usr/bin/env python3
"""Generates the FAVDAVCON AND CG NIG LTD corporate website (15 static pages)."""
import os

BRAND = "FAVDAVCON AND CG NIG LTD"
PHONE1, PHONE2 = "0706 341 5883", "0901 684 1290"
TEL1 = "+2347063415883"
WA = "2347063415883"
EMAIL = "imeguchristopher@gmail.com"
ADDR = "No 45, Abuja Million Estate, Aso Rock Villa, Guzape, Abuja, FCT, Nigeria"

CATS = [
 ("uniforms", "Uniforms & Accoutrements", "camo",
  "High-quality camouflage, OG greens (Tetrons), caps, berets, buttons and full ceremonial kit — imported and supplied to specification.",
  [("camo","Camouflage Uniforms","Combat camouflage sets produced to service specification, in full size ranges."),
   ("greens","Ceremonial & OG Green Uniforms","OG greens (Tetrons) and ceremonial dress for parades and formal duties."),
   ("calendar","Caps, Berets & Insignia","Caps, berets, buttons, badges and rank insignia to regulation standard.")]),
 ("boots-field-kit", "Boots & Field Kit", "boots",
  "Imported combat boots, night-vision equipment and field kit built for durability in demanding conditions.",
  [("boots","Combat Boots","Durable military-grade boots and footwear, supplied in bulk across all sizes."),
   ("nightvision","Night Vision Equipment","Night-vision goggles and optical equipment for night operations."),
   ("camo","Field Kit & Accessories","Webbing, kit bags and field accessories to complete the soldier's loadout.")]),
 ("security-systems", "Security Systems & Consultancy", "drone",
  "Security consultancy services and supply of surveillance and communications equipment — drones, CCTV, radios and more.",
  [("consult","Security Consultancy","Professional advisory on security architecture, assessments and planning."),
   ("cctv","CCTV Surveillance Systems","Camera systems, DVR/NVR equipment and monitoring infrastructure."),
   ("install","Installation & Maintenance","Professional installation, configuration and after-supply support."),
   ("radios","Two-Way Radio Communications","Professional handheld radios and charging systems for coordinated operations."),
   ("drone","Surveillance Drones","Drone systems for aerial surveillance, monitoring and reconnaissance.")]),
 ("office-supply", "Office Furniture & Equipment", "desk1",
  "Complete office fit-out: executive furniture, computers, printing machines, safes and workstations for institutions.",
  [("desk1","Executive Office Furniture","Executive desks, conference suites and office seating."),
   ("desk2","Office Desk Sets","Complete desk and chair sets for administrative offices."),
   ("computers","Computer Workstations","Bulk supply and setup of computer workstations and ICT rooms."),
   ("copier","Photocopiers & Printing Machines","Heavy-duty copiers and printing machines for institutional use."),
   ("cabinet","Storage & Filing Cabinets","Secure storage and filing solutions for offices."),
   ("safe","Security Safes","Fire-resistant safes for documents, valuables and sensitive items.")]),
 ("vehicles", "Operational Vehicles", "truck",
  "Supply of all types of operational vehicles — troop-carrying trucks, staff buses and utility fleets.",
  [("truck","Operational Trucks","Heavy-duty covered trucks for logistics, transport and operations."),
   ("bus","Staff & Troop Buses","Coaches and buses for personnel movement and institutional transport.")]),
 ("printing-services", "Printing & Environmental Services", "printer",
  "General printing — from branded stationery to large-format work — plus beautification and fumigation services.",
  [("printer","Large-Format & General Printing","Banners, documents and large-format printing on modern machines."),
   ("notebooks","Branded Notebooks & Stationery","Corporate notebooks, jotters and official stationery."),
   ("bag","Branded Bags & Packaging","Custom-branded bags and premium packaging."),
   ("calendar","Calendars & Corporate Items","Calendars, diaries and corporate gift items."),
   ("consult","Environmental Services","Beautification and fumigation services for premises and facilities.")]),
]

REGS = [
 ("CAC Incorporation", "RC 7971283", "Corporate Affairs Commission — incorporated under CAMA 2020"),
 ("Bureau of Public Procurement", "Ref 0000-0018-5065", "Registered federal contractor and service provider"),
 ("SCUML (EFCC)", "RN SC 152116691", "Special Control Unit Against Money Laundering registration"),
 ("PenCom Clearance", "PR0000126716", "Pension Reform Act 2014 compliance"),
 ("NSITF Clearance", "Reg 1008422325", "Employees' Compensation Act 2010 compliance"),
 ("ITF Compliance", "BAU-012-9330", "Industrial Training Fund contribution compliance"),
]

CSS = """
:root{--olive:#232D1E;--olive-2:#2E3A27;--dark:#151C10;--gold:#C9A85C;--gold-d:#A9852F;--paper:#F4F3EC;--white:#FFFFFF;--ink:#1E2419;--ink-soft:#565E4E;--muted:#AEB8A2;
--disp:'Oswald',sans-serif;--body:'Source Sans 3',sans-serif}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--paper);color:var(--ink);font-family:var(--body);line-height:1.7;-webkit-font-smoothing:antialiased}
img{display:block;max-width:100%}a{color:inherit}
h1,h2,h3{font-family:var(--disp);font-weight:600;line-height:1.2;letter-spacing:.02em;text-transform:uppercase}
.wrap{max-width:1120px;margin:0 auto;padding:0 22px}
.eyebrow{color:var(--gold-d);font-weight:700;font-size:.76rem;letter-spacing:.2em;text-transform:uppercase;display:block;margin-bottom:12px}
.btn{display:inline-flex;align-items:center;gap:8px;background:var(--gold);color:var(--dark);font-family:var(--disp);font-weight:600;font-size:.9rem;letter-spacing:.08em;text-transform:uppercase;padding:14px 26px;text-decoration:none;border:none;cursor:pointer;transition:background .15s,transform .15s}
.btn:hover{background:#DDBE74;transform:translateY(-2px)}
.btn-line{background:transparent;color:var(--white);border:1px solid rgba(255,255,255,.4)}
.btn-line:hover{background:rgba(255,255,255,.08)}
.top{position:sticky;top:0;z-index:80;background:var(--dark);border-bottom:2px solid var(--gold)}
.top-in{max-width:1120px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;gap:12px;padding:10px 22px}
.brand{display:flex;align-items:center;gap:11px;text-decoration:none;color:var(--white)}
.brand .lg{background:var(--white);border-radius:6px;padding:3px;width:44px;height:44px;display:flex;align-items:center;justify-content:center;flex:none}
.brand .lg img{max-height:38px;width:auto}
.brand-name{font-family:var(--disp);font-size:.95rem;line-height:1.25;letter-spacing:.05em}
.brand-name small{display:block;font-family:var(--body);font-size:.6rem;letter-spacing:.24em;color:var(--gold);text-transform:uppercase}
.nav-links{display:none;gap:24px;list-style:none;align-items:center}
.nav-links>li{position:relative}
.nav-links a{text-decoration:none;font-weight:600;font-size:.82rem;letter-spacing:.06em;color:#C9CFC0;text-transform:uppercase;padding:8px 0}
.nav-links a:hover,.nav-links a.on{color:var(--gold)}
.burger{background:none;border:1px solid var(--gold);color:var(--gold);font-size:1.4rem;line-height:1;cursor:pointer;padding:6px 11px}
.mnav{display:none;background:var(--olive);border-top:1px solid rgba(255,255,255,.1)}
.mnav.open{display:block}
.mnav a{display:block;padding:14px 22px;text-decoration:none;color:#E7EADF;font-weight:600;font-size:.9rem;border-bottom:1px solid rgba(255,255,255,.07)}
.mnav a:hover{color:var(--gold)}
.mnav .sub{padding-left:40px;font-size:.83rem;color:var(--muted)}
@media(min-width:980px){.nav-links{display:flex}.burger,.mnav{display:none!important}}
.hero{position:relative;isolation:isolate;min-height:74vh;display:flex;align-items:center;padding:64px 0;color:var(--white)}
.hero::before{content:"";position:absolute;inset:0;z-index:-2;background:url('img/hero.webp') center 30%/cover no-repeat}
.hero::after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(100deg,rgba(13,17,9,.95) 30%,rgba(13,17,9,.75) 58%,rgba(21,28,16,.42))}
.hero h1{font-size:clamp(2rem,5.2vw,3.5rem);max-width:19ch}
.hero h1 em{font-style:normal;color:var(--gold)}
.hero p{color:#D6DBCB;font-size:1.06rem;max-width:56ch;margin:18px 0 28px}
.hero-cta{display:flex;gap:14px;flex-wrap:wrap}
.hero-reg{margin-top:30px;font-size:.76rem;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
.band{background:var(--gold)}
.band-in{max-width:1120px;margin:0 auto;padding:24px 22px;display:grid;grid-template-columns:repeat(2,1fr);gap:14px;text-align:center;color:var(--dark)}
.band b{display:block;font-family:var(--disp);font-size:1.5rem}
.band span{font-size:.72rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase}
@media(min-width:760px){.band-in{grid-template-columns:repeat(4,1fr)}}
.sec{padding:66px 0}
.sec.dark{background:var(--olive);color:var(--white)}
.sec.white{background:var(--white)}
.sec-head{margin-bottom:34px;max-width:70ch}
.sec-head h2{font-size:clamp(1.6rem,4vw,2.4rem)}
.sec-head p{color:var(--ink-soft);margin-top:10px}
.sec.dark .sec-head p{color:var(--muted)}
.grid{display:grid;gap:18px}
@media(min-width:700px){.grid.g2{grid-template-columns:1fr 1fr}.grid.g3{grid-template-columns:repeat(3,1fr)}}
.card{background:var(--white);border:1px solid #DCDACC;text-decoration:none;display:flex;flex-direction:column;transition:transform .18s,box-shadow .18s}
.card:hover{transform:translateY(-4px);box-shadow:0 16px 34px rgba(21,28,16,.16)}
.card .im{aspect-ratio:16/10.5;overflow:hidden;background:#E7E5DA}
.card .im img{width:100%;height:100%;object-fit:cover;transition:transform .3s}
.card:hover .im img{transform:scale(1.05)}
.card .bd{padding:20px 20px 22px;display:flex;flex-direction:column;gap:8px;flex:1}
.card h3{font-size:1.05rem;color:var(--olive)}
.card p{font-size:.92rem;color:var(--ink-soft);flex:1}
.card .go{font-family:var(--disp);font-size:.8rem;letter-spacing:.1em;text-transform:uppercase;color:var(--gold-d)}
.pagehero{background:var(--olive);color:var(--white);padding:58px 0}
.pagehero h1{font-size:clamp(1.9rem,5vw,3rem)}
.pagehero p{color:var(--muted);margin-top:12px;max-width:64ch;font-size:1.03rem}
.crumb{font-size:.78rem;letter-spacing:.1em;text-transform:uppercase;color:var(--gold);margin-bottom:14px}
.crumb a{color:var(--gold);text-decoration:none}.crumb a:hover{text-decoration:underline}
.regs{display:grid;gap:14px}
@media(min-width:760px){.regs{grid-template-columns:repeat(3,1fr)}}
.reg{background:rgba(255,255,255,.05);border:1px solid rgba(201,168,92,.35);padding:22px}
.reg b{font-family:var(--disp);display:block;font-size:.98rem;letter-spacing:.04em;text-transform:uppercase;color:var(--gold)}
.reg .no{font-size:.8rem;letter-spacing:.08em;color:var(--white);margin:4px 0 8px;font-weight:700}
.reg p{font-size:.85rem;color:var(--muted)}
.split{display:grid;gap:36px;align-items:center}
@media(min-width:860px){.split{grid-template-columns:1fr 1.2fr}}
.portrait{position:relative;max-width:360px}
.portrait img{width:100%;border:1px solid #D8D5C6}
.portrait::before{content:"";position:absolute;right:-13px;bottom:-13px;width:80%;height:55%;background:var(--olive);z-index:-1}
.portrait::after{content:"";position:absolute;top:-13px;left:-13px;width:72px;height:72px;border-top:4px solid var(--gold);border-left:4px solid var(--gold)}
.f-card{background:var(--white);border:1px solid #DCDACC;padding:32px 26px;max-width:760px;margin:0 auto}
.f-row{margin-bottom:16px}
.f-row label{display:block;font-family:var(--disp);font-weight:600;font-size:.76rem;letter-spacing:.12em;text-transform:uppercase;color:var(--olive);margin-bottom:7px}
.f-row input,.f-row select,.f-row textarea{width:100%;background:var(--paper);border:1px solid #C9C6B6;color:var(--ink);padding:13px;font-family:var(--body);font-size:1rem}
.f-row textarea{min-height:130px;resize:vertical}
.f-row input:focus,.f-row select:focus,.f-row textarea:focus{border-color:var(--gold-d);outline:none}
.f-note{font-size:.8rem;color:var(--ink-soft);margin-top:14px}
.ccards{display:grid;gap:14px}
@media(min-width:760px){.ccards{grid-template-columns:repeat(3,1fr)}}
.ccard{background:var(--white);border:1px solid #DCDACC;padding:24px;text-align:center}
.ccard h3{font-size:.95rem;color:var(--olive);margin:8px 0 8px}
.ccard p{font-size:.92rem;color:var(--ink-soft)}
.ccard a{font-weight:700;color:var(--gold-d)}
.legal h2{font-size:1.2rem;margin:28px 0 10px;color:var(--olive)}
.legal p,.legal li{color:var(--ink-soft);margin-bottom:12px}.legal ul{padding-left:22px}
footer{background:var(--dark);color:#B9BFAD;padding:46px 22px 26px}
.f-grid{max-width:1120px;margin:0 auto;display:grid;gap:28px}
@media(min-width:760px){.f-grid{grid-template-columns:1.4fr 1fr 1fr}}
footer .f-brand{font-family:var(--disp);font-size:1.1rem;color:var(--white);letter-spacing:.05em;text-transform:uppercase;margin-bottom:10px}
footer p,footer a{font-size:.88rem}
footer a{color:#B9BFAD;text-decoration:none}footer a:hover{color:var(--gold)}
footer h4{font-family:var(--disp);color:var(--gold);font-size:.82rem;letter-spacing:.14em;text-transform:uppercase;margin-bottom:12px}
footer li{list-style:none;margin-bottom:8px}
.f-bottom{max-width:1120px;margin:28px auto 0;padding-top:18px;border-top:1px solid rgba(255,255,255,.12);font-size:.78rem;display:flex;flex-wrap:wrap;gap:10px;justify-content:space-between}
"""

def nav(active):
    items = [("index.html","Home"),("about.html","About"),("products.html","Products & Services"),("leadership.html","Leadership"),("contact.html","Contact")]
    links = "".join(f'<li><a href="{h}" class="{"on" if h==active else ""}">{t}</a></li>' for h,t in items)
    mob = "".join(f'<a href="{h}">{t}</a>' for h,t in items)
    mobcats = "".join(f'<a class="sub" href="{s}.html">{t}</a>' for s,t,*_ in [(c[0],c[1]) for c in CATS])
    return f"""<header class="top"><div class="top-in">
<a class="brand" href="index.html"><span class="lg"><img src="img/logo.webp" alt="{BRAND} logo"></span>
<span class="brand-name">Favdavcon &amp; CG Nig Ltd<small>Military &amp; Corporate Supply</small></span></a>
<nav><ul class="nav-links">{links}<li><a class="btn" style="padding:10px 18px" href="quote.html">Request a Quote</a></li></ul>
<button class="burger" aria-label="Menu" onclick="document.getElementById('mnav').classList.toggle('open')">&#9776;</button></nav></div>
<div class="mnav" id="mnav">{mob}{mobcats}<a href="quote.html" style="color:var(--gold)">Request a Quote</a></div></header>"""

FOOTER = f"""<footer><div class="f-grid">
<div><div class="f-brand">{BRAND}</div>
<p>Military &amp; paramilitary procurement, security systems, office supply, operational vehicles and printing services. Incorporated under CAMA 2020 — RC 7971283.</p>
<p style="margin-top:10px">{ADDR}</p></div>
<div><h4>Products &amp; Services</h4><ul>""" + "".join(f'<li><a href="{c[0]}.html">{c[1]}</a></li>' for c in CATS) + f"""</ul></div>
<div><h4>Company</h4><ul><li><a href="about.html">About Us</a></li><li><a href="leadership.html">Leadership</a></li><li><a href="quote.html">Request a Quote</a></li><li><a href="contact.html">Contact</a></li><li><a href="terms.html">Terms &amp; Conditions</a></li><li><a href="privacy.html">Privacy Policy</a></li></ul></div></div>
<div class="f-bottom"><span>© 2026 {BRAND}. All rights reserved.</span><span>RC 7971283 · BPP Ref 0000-0018-5065 · SCUML RN SC 152116691</span></div></footer>"""

def page(fname, title, desc, active, body):
    html = f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@500;600&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
<link rel="icon" href="img/logo.webp">
</head><body>
{nav(active)}
{body}
{FOOTER}
</body></html>"""
    open(fname, "w").write(html)

os.makedirs(".", exist_ok=True)
open("styles.css","w").write(CSS)

# ---------- INDEX ----------
cat_cards = "".join(f"""<a class="card" href="{s}.html"><div class="im"><img src="img/{img}.webp" alt="{t}" loading="lazy"></div>
<div class="bd"><h3>{t}</h3><p>{intro}</p><span class="go">View Products →</span></div></a>""" for s,t,img,intro,_ in CATS)
regs_html = "".join(f'<div class="reg"><b>{a}</b><span class="no">{b}</span><p>{c}</p></div>' for a,b,c in REGS)

index_body = f"""
<section class="hero"><div class="wrap">
<span class="eyebrow" style="color:var(--gold)">Abuja · Federal Contractor · RC 7971283</span>
<h1>Equipping those who <em>defend the nation.</em></h1>
<p>FAVDAVCON AND CG NIG LTD is a technology-oriented supply company serving Nigeria's military, paramilitary and corporate institutions — led by a retired Army officer with over three decades of service, including procurement legal oversight at Army Headquarters.</p>
<div class="hero-cta"><a class="btn" href="quote.html">Request a Quote</a><a class="btn btn-line" href="products.html">Our Products &amp; Services</a></div>
<div class="hero-reg">CAC · BPP · SCUML · PenCom · NSITF · ITF Registered &amp; Compliant</div>
</div></section>
<div class="band"><div class="band-in">
<div><b>34+ Yrs</b><span>Military Experience</span></div>
<div><b>6</b><span>Supply Categories</span></div>
<div><b>6</b><span>Federal Registrations</span></div>
<div><b>Abuja</b><span>Nationwide Delivery</span></div>
</div></div>
<section class="sec"><div class="wrap">
<div class="sec-head"><span class="eyebrow">What We Supply</span><h2>Products &amp; Services</h2>
<p>From uniforms and field kit to vehicles, security systems and complete office fit-outs — every category is handled to institutional standard.</p></div>
<div class="grid g3">{cat_cards}</div>
</div></section>
<section class="sec dark"><div class="wrap">
<div class="sec-head"><span class="eyebrow">Why Institutions Trust Us</span><h2>Fully Registered. Fully Compliant.</h2>
<p>Procurement begins with paperwork. Ours is complete — six federal registrations and clearances held and current.</p></div>
<div class="regs">{regs_html}</div>
</div></section>
<section class="sec white"><div class="wrap split">
<div class="portrait"><img src="img/ceo.webp" alt="Major Barr. Christopher Onowoakpor Imegu (rtd), CEO"></div>
<div><span class="eyebrow">Leadership</span>
<h2 style="font-size:clamp(1.5rem,3.6vw,2.2rem)">Led by 34 years inside the system we serve</h2>
<p style="color:var(--ink-soft);margin:14px 0">Our CEO, Major Barr. Christopher Onowoakpor Imegu (rtd), served the Nigerian Army for over three decades — including as Deputy Director Legal Services and Procurement Legal Officer at Army Headquarters. We understand what the Armed Forces need, and exactly how they procure it.</p>
<a class="btn" href="leadership.html">Meet Our Leadership</a></div>
</div></section>
<section class="sec dark" style="text-align:center"><div class="wrap">
<h2 style="font-size:clamp(1.5rem,4vw,2.2rem)">Have a supply requirement?</h2>
<p style="color:var(--muted);margin:12px auto 26px;max-width:52ch">Tell us what your institution needs and receive a formal quotation promptly.</p>
<a class="btn" href="quote.html">Request a Quote</a>
</div></section>"""
page("index.html", f"{BRAND} — Military & Corporate Supply, Abuja", "Military and paramilitary procurement, security systems, office supply, operational vehicles and printing services. RC 7971283, BPP-registered federal contractor in Abuja.", "index.html", index_body)

# ---------- ABOUT ----------
about_body = f"""
<section class="pagehero"><div class="wrap"><div class="crumb"><a href="index.html">Home</a> / About</div>
<h1>About the Company</h1>
<p>A top-notch, technology-oriented supply company incorporated to serve Nigeria's military, paramilitary and corporate institutions.</p></div></section>
<section class="sec"><div class="wrap" style="max-width:820px">
<span class="eyebrow">Who We Are</span>
<h2 style="margin-bottom:16px">Bridging the gaps in military logistics</h2>
<p style="color:var(--ink-soft);margin-bottom:14px">FAVDAVCON AND CG NIG LTD was incorporated on 2nd October 2024 under the Companies and Allied Matters Act 2020 (RC 7971283). Our services range from military and paramilitary procurement of accoutrements — uniform materials and kits — to office furniture, operational vehicles, printing services, environmental services such as beautification and fumigation, and security and corporate services.</p>
<p style="color:var(--ink-soft);margin-bottom:14px">No army in the world succeeds without logistics. Our purpose is to complement the Nigerian Armed Forces and paramilitary organisations with the supply of quality accoutrements for the adequate and smart functioning of the system.</p>
<div class="grid g2" style="margin-top:30px">
<div class="reg" style="background:var(--white);border-color:#D6D3C2"><b style="color:var(--olive)">Our Vision</b><p style="color:var(--ink-soft);margin-top:8px">To supply military accoutrement, office equipment and all other accessories that enable the military to perform their roles effectively and efficiently.</p></div>
<div class="reg" style="background:var(--white);border-color:#D6D3C2"><b style="color:var(--olive)">Our Mission</b><p style="color:var(--ink-soft);margin-top:8px">To ensure our military and paramilitary function adequately for the sustenance of peace and security in Nigeria.</p></div>
</div></div></section>
<section class="sec dark"><div class="wrap">
<div class="sec-head"><span class="eyebrow">Registrations &amp; Compliance</span><h2>Our Credentials</h2>
<p>Every registration a procuring entity expects — held and current.</p></div>
<div class="regs">{regs_html}</div></div></section>
<section class="sec" style="text-align:center"><div class="wrap">
<a class="btn" href="quote.html">Request a Quote</a></div></section>"""
page("about.html", f"About Us — {BRAND}", "About FAVDAVCON AND CG NIG LTD: vision, mission and full federal registrations — CAC, BPP, SCUML, PenCom, NSITF, ITF.", "about.html", about_body)

# ---------- PRODUCTS HUB ----------
prod_body = f"""
<section class="pagehero"><div class="wrap"><div class="crumb"><a href="index.html">Home</a> / Products &amp; Services</div>
<h1>Products &amp; Services</h1>
<p>Six supply categories, one standard: quality materials, correct specification, dependable delivery. Select a category to view products.</p></div></section>
<section class="sec"><div class="wrap"><div class="grid g3">{cat_cards}</div></div></section>
<section class="sec dark" style="text-align:center"><div class="wrap">
<h2 style="font-size:clamp(1.4rem,4vw,2rem)">Don't see exactly what you need?</h2>
<p style="color:var(--muted);margin:12px auto 24px;max-width:52ch">We procure to specification. Describe your requirement and we will source it.</p>
<a class="btn" href="quote.html">Request a Quote</a></div></section>"""
page("products.html", f"Products & Services — {BRAND}", "Uniforms and accoutrements, boots and field kit, security systems, office supply, operational vehicles, printing and environmental services.", "products.html", prod_body)

# ---------- CATEGORY PAGES ----------
for slug, title, heroimg, intro, items in CATS:
    cards = "".join(f"""<div class="card"><div class="im"><img src="img/{im}.webp" alt="{nm}" loading="lazy"></div>
<div class="bd"><h3>{nm}</h3><p>{ds}</p><a class="go" href="quote.html?c={slug}">Request Quote →</a></div></div>""" for im,nm,ds in items)
    body = f"""
<section class="pagehero"><div class="wrap"><div class="crumb"><a href="index.html">Home</a> / <a href="products.html">Products &amp; Services</a> / {title}</div>
<h1>{title}</h1><p>{intro}</p></div></section>
<section class="sec"><div class="wrap"><div class="grid g3">{cards}</div>
<p style="margin-top:30px;color:var(--ink-soft)">All items are supplied to institutional specification and in bulk quantities. Pricing is provided by formal quotation.</p>
<div style="margin-top:20px"><a class="btn" href="quote.html?c={slug}">Request a Quote for {title}</a></div>
</div></section>"""
    page(f"{slug}.html", f"{title} — {BRAND}", f"{intro}", "products.html", body)

# ---------- LEADERSHIP ----------
lead_body = f"""
<section class="pagehero"><div class="wrap"><div class="crumb"><a href="index.html">Home</a> / Leadership</div>
<h1>Our Leadership</h1><p>Decades of service. Deep institutional knowledge. Uncompromising standards.</p></div></section>
<section class="sec white"><div class="wrap split">
<div class="portrait"><img src="img/ceo.webp" alt="Major Barr. Christopher Onowoakpor Imegu (rtd), Chief Executive Officer"></div>
<div><span class="eyebrow">Chief Executive Officer</span>
<h2 style="font-size:clamp(1.5rem,3.8vw,2.2rem)">Major Barr. Christopher Onowoakpor Imegu (rtd)</h2>
<p style="color:var(--gold-d);font-weight:700;letter-spacing:.08em;font-size:.85rem;text-transform:uppercase;margin:8px 0 16px">LL.B · B.L · LL.M · Ph.D (in view) · Dip. Security Management</p>
<p style="color:var(--ink-soft);margin-bottom:12px">Enlisted into the Nigerian Army in 1990 and commissioned in 2002, our CEO rose to the rank of Major before his voluntary retirement in June 2024 — after 34 years and six months of service.</p>
<p style="color:var(--ink-soft);margin-bottom:12px">Commissioned into the Nigerian Army Ordinance Corps, he was subsequently seconded to the Directorate of Legal Services, where he served for nearly two decades — including as SO2 Military Justice, Legal Officer at the Directorate of Legal Services, and Deputy Director Legal Services at Army Headquarters, where he doubled as Procurement Legal Officer. He later served as Deputy Director Legal Services at 3 Division Headquarters, Division Legal Adviser to the GOC 3 Armoured Division, at Defence Headquarters Garrison, Mogadishu Cantonment, and finally with 7 Division Legal Services as Legal Adviser to the GOC.</p>
<p style="color:var(--ink-soft);margin-bottom:12px">His military education includes the Ordinance Basic Course, Young Infantry Course, Military Justice, Legal Aspects of Counter-Terrorism (United States), and Junior and Senior Courses at the Armed Forces Command and Staff College, Jaji.</p>
<p style="color:var(--ink-soft)">That experience — inside military procurement itself — is the foundation of FAVDAVCON AND CG NIG LTD: there is no doubt that quality and suitable materials will be procured, toward an Army adequately kitted for the sustenance of peace and security in Nigeria.</p>
</div></div></section>
<section class="sec dark" style="text-align:center"><div class="wrap">
<a class="btn" href="quote.html">Request a Quote</a></div></section>"""
page("leadership.html", f"Leadership — {BRAND}", "Major Barr. Christopher Onowoakpor Imegu (rtd), CEO — 34 years of Nigerian Army service including procurement legal oversight at Army Headquarters.", "leadership.html", lead_body)

# ---------- QUOTE ----------
opts = "".join(f"<option value=\"{t}\">{t}</option>" for _,t,_,_,_ in CATS) + "<option>Other / Multiple Categories</option>"
quote_body = f"""
<section class="pagehero"><div class="wrap"><div class="crumb"><a href="index.html">Home</a> / Request a Quote</div>
<h1>Request a Quote</h1><p>Describe your requirement and our team will respond with a formal quotation promptly. All enquiries are treated in confidence.</p></div></section>
<section class="sec"><div class="wrap"><div class="f-card">
<form action="https://formsubmit.co/{EMAIL}" method="POST">
<input type="hidden" name="_subject" value="QUOTE REQUEST — Favdavcon Website">
<input type="hidden" name="_template" value="table"><input type="hidden" name="_captcha" value="false">
<div class="f-row"><label for="q-name">Contact Name</label><input id="q-name" name="Name" required placeholder="e.g. Capt. A. Bello / Mrs. Ada Obi"></div>
<div class="f-row"><label for="q-org">Organisation / Institution</label><input id="q-org" name="Organisation" required placeholder="e.g. Ministry, unit, company"></div>
<div class="f-row"><label for="q-phone">Phone Number</label><input id="q-phone" name="Phone" type="tel" required placeholder="e.g. 0803 000 0000"></div>
<div class="f-row"><label for="q-email">Email Address</label><input id="q-email" name="Email" type="email" placeholder="optional"></div>
<div class="f-row"><label for="q-cat">Category</label><select id="q-cat" name="Category">{opts}</select></div>
<div class="f-row"><label for="q-desc">Requirement Details</label><textarea id="q-desc" name="Details" required placeholder="Items, quantities, specifications, timelines…"></textarea></div>
<button class="btn" type="submit">Submit Quote Request</button>
<p class="f-note">Prefer to talk? Call {PHONE1} or <a href="https://wa.me/{WA}?text=Good%20day%2C%20I%20would%20like%20to%20request%20a%20quotation%20from%20FAVDAVCON%20AND%20CG%20NIG%20LTD." target="_blank" rel="noopener" style="color:var(--gold-d);font-weight:700">message us on WhatsApp</a>.</p>
</form></div></div></section>
<script>
const c=new URLSearchParams(location.search).get('c');
if(c){{const map={{{",".join(f'"{s}":"{t}"' for s,t,_,_,_ in CATS)}}};const v=map[c];const s=document.getElementById('q-cat');if(v)s.value=v;}}
</script>"""
page("quote.html", f"Request a Quote — {BRAND}", "Request a formal quotation for uniforms, field kit, security systems, office supply, vehicles or printing services.", "quote.html", quote_body)

# ---------- CONTACT ----------
contact_body = f"""
<section class="pagehero"><div class="wrap"><div class="crumb"><a href="index.html">Home</a> / Contact</div>
<h1>Contact Us</h1><p>Reach the corporate office directly, or submit a quote request online.</p></div></section>
<section class="sec"><div class="wrap"><div class="ccards">
<div class="ccard"><div style="font-size:1.4rem">📍</div><h3>Corporate Office</h3><p>{ADDR}</p><p style="margin-top:8px"><a href="https://www.google.com/maps/search/?api=1&query=Abuja+Million+Estate+Guzape+Abuja" target="_blank" rel="noopener">Open in Google Maps</a></p></div>
<div class="ccard"><div style="font-size:1.4rem">📞</div><h3>Phone &amp; WhatsApp</h3><p><a href="tel:{TEL1}">{PHONE1}</a><br><a href="tel:+234{PHONE2.replace(' ','')[1:]}">{PHONE2}</a></p><p style="margin-top:8px"><a href="https://wa.me/{WA}" target="_blank" rel="noopener">Chat on WhatsApp</a></p></div>
<div class="ccard"><div style="font-size:1.4rem">✉️</div><h3>Email</h3><p><a href="mailto:{EMAIL}">{EMAIL}</a></p><p style="margin-top:8px">We respond promptly to all institutional enquiries.</p></div>
</div>
<div style="text-align:center;margin-top:36px"><a class="btn" href="quote.html">Request a Quote</a></div>
</div></section>"""
page("contact.html", f"Contact — {BRAND}", f"Contact FAVDAVCON AND CG NIG LTD — {ADDR}. Phone {PHONE1}.", "contact.html", contact_body)

# ---------- LEGAL ----------
terms_body = f"""
<section class="pagehero"><div class="wrap"><h1>Terms &amp; Conditions</h1><p>Terms of use of the {BRAND} website. Last updated: July 2026.</p></div></section>
<section class="sec legal"><div class="wrap" style="max-width:800px">
<h2>1. About this website</h2><p>This website is operated by {BRAND} ("the Company"), RC 7971283, of {ADDR}. By using this website you agree to these terms.</p>
<h2>2. Information only</h2><p>Content on this website is provided for general information about the Company and its products and services. It does not constitute an offer; all supplies are subject to formal quotation, purchase order and contract.</p>
<h2>3. Quotations</h2><p>Quotation requests submitted through this website are invitations to treat. Prices, specifications and availability are confirmed only in a formal written quotation from the Company.</p>
<h2>4. Intellectual property</h2><p>All content on this website belongs to the Company or its licensors and may not be reproduced without written permission.</p>
<h2>5. Accuracy and availability</h2><p>The Company takes reasonable care to keep this website accurate and available but does not guarantee it will be error-free or uninterrupted, and may amend content at any time.</p>
<h2>6. Limitation of liability</h2><p>To the fullest extent permitted by law, the Company accepts no liability for loss arising from reliance on general information on this website.</p>
<h2>7. Governing law</h2><p>These terms are governed by the laws of the Federal Republic of Nigeria.</p>
<h2>8. Contact</h2><p>Questions may be directed to {EMAIL} or {PHONE1}.</p>
</div></section>"""
page("terms.html", f"Terms & Conditions — {BRAND}", "Terms of use of the FAVDAVCON AND CG NIG LTD website.", "", terms_body)

privacy_body = f"""
<section class="pagehero"><div class="wrap"><h1>Privacy Policy</h1><p>How {BRAND} handles your information. Last updated: July 2026.</p></div></section>
<section class="sec legal"><div class="wrap" style="max-width:800px">
<h2>1. Who we are</h2><p>{BRAND} ("the Company"), RC 7971283, of {ADDR}, is committed to protecting your privacy in line with the Nigeria Data Protection Act.</p>
<h2>2. Information we collect</h2><ul><li><strong>Quote requests</strong> — the details you submit: name, organisation, phone, email and requirement description.</li><li><strong>Correspondence</strong> — records of communications with us by phone, WhatsApp or email.</li></ul><p>This website does not use tracking or advertising cookies.</p>
<h2>3. How we use information</h2><p>Solely to respond to your enquiry, prepare quotations, perform contracts, maintain business records and comply with legal obligations. We do not sell your information.</p>
<h2>4. Form delivery</h2><p>Requests submitted through the website form are transmitted to the Company's email via a form-delivery service. By submitting, you consent to this transmission.</p>
<h2>5. Disclosure</h2><p>We do not disclose your information to third parties except as necessary to fulfil your request or where required by law.</p>
<h2>6. Retention</h2><p>Information is retained only as long as necessary for the purposes above and applicable record-keeping obligations.</p>
<h2>7. Your rights</h2><p>You may request access to, correction of, or deletion of your personal information by contacting us.</p>
<h2>8. Contact</h2><p>{EMAIL} · {PHONE1}</p>
</div></section>"""
page("privacy.html", f"Privacy Policy — {BRAND}", "Privacy policy of the FAVDAVCON AND CG NIG LTD website.", "", privacy_body)

thanks_body = f"""
<section class="pagehero" style="min-height:56vh;display:flex;align-items:center"><div class="wrap" style="text-align:center;width:100%">
<h1 style="color:var(--gold)">Request Received</h1>
<p style="margin:14px auto 26px">Thank you — your quote request has been received. Our team will respond promptly. For urgent requirements, call <a href="tel:{TEL1}" style="color:var(--white);font-weight:700">{PHONE1}</a>.</p>
<a class="btn" href="index.html">Return to Website</a></div></section>"""
page("thanks.html", f"Request Received — {BRAND}", "Your quote request has been received.", "", thanks_body)

print("Generated pages:", len([f for f in os.listdir('.') if f.endswith('.html')]))
