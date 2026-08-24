import os

base = r'C:\Users\msshi\Desktop\NöraL-website\public'

NAV = """<nav>
  <a href="index.html" class="nav-logo">
    <img src="images/logo.jpg" alt="NöraL Logo">
    <span class="nav-logo-text">NöraL</span>
  </a>
  <ul class="nav-links">
    <li><a href="index.html"><span class="en">Home</span><span class="tr">Ana Sayfa</span></a></li>
    <li><a href="people.html"><span class="en">People</span><span class="tr">Ekip</span></a></li>
    <li><a href="studies.html"><span class="en">Studies</span><span class="tr">&#199;al&#305;&#351;malar</span></a></li>
    <li><a href="news.html"><span class="en">News</span><span class="tr">Haberler</span></a></li>
    <li><a href="contact.html" class="btn-nav"><span class="en">Contact</span><span class="tr">&#304;leti&#351;im</span></a></li>
  </ul>
  <button id="lang-toggle" class="lang-btn">TR</button>
  <div class="hamburger"><span></span><span></span><span></span></div>
</nav>"""

FOOTER = """<footer>
  <div class="footer-inner">
    <div class="footer-top">
      <div class="footer-brand">
        <div class="footer-logo"><img src="images/logo.jpg" alt="NöraL"><span>NöraL</span></div>
        <p class="footer-desc"><span class="en">Neuroscience research, learning and collaboration community.</span><span class="tr">N&#246;robilim ara&#351;t&#305;rma ve i&#351;birli&#287;i toplulu&#287;u.</span></p>
        <div class="footer-socials"><a href="#">ig</a><a href="#">tw</a><a href="#">in</a><a href="#">tg</a></div>
      </div>
      <div class="footer-col">
        <h4><span class="en">Pages</span><span class="tr">Sayfalar</span></h4>
        <ul>
          <li><a href="index.html"><span class="en">Home</span><span class="tr">Ana Sayfa</span></a></li>
          <li><a href="people.html"><span class="en">People</span><span class="tr">Ekip</span></a></li>
          <li><a href="studies.html"><span class="en">Studies</span><span class="tr">&#199;al&#305;&#351;malar</span></a></li>
          <li><a href="news.html"><span class="en">News</span><span class="tr">Haberler</span></a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4><span class="en">Community</span><span class="tr">Topluluk</span></h4>
        <ul>
          <li><a href="contact.html"><span class="en">Contact</span><span class="tr">&#304;leti&#351;im</span></a></li>
          <li><a href="#"><span class="en">Privacy Policy</span><span class="tr">Gizlilik Politikas&#305;</span></a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4><span class="en">Contact</span><span class="tr">&#304;leti&#351;im</span></h4>
        <ul>
          <li><a href="mailto:info@NöraL.com">info@NöraL.com</a></li>
          <li><a href="#">Instagram</a></li>
          <li><a href="#">Telegram</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 NöraL <span class="en">Neuroscience Community</span><span class="tr">N&#246;robilim Toplulu&#287;u</span></span>
      <a href="#"><span class="en">Privacy Policy</span><span class="tr">Gizlilik</span></a>
    </div>
  </div>
</footer>
<script src="js/main.js"></script>
</body>
</html>"""

CTA = """<div class="cta-banner">
  <div class="cta-banner-content">
    <h2><span class="en">Ready to Join?</span><span class="tr">Kat&#305;lmaya Haz&#305;r m&#305;s&#305;n?</span></h2>
    <p><span class="en">Lorem ipsum dolor sit amet. Curiosity is all you need.</span><span class="tr">Lorem ipsum dolor sit amet. Merak&#305;n yeterli.</span></p>
    <a href="contact.html" class="btn btn-primary"><span class="en">Get in Touch &rarr;</span><span class="tr">&#304;leti&#351;ime Ge&#231; &rarr;</span></a>
  </div>
</div>"""

def page(title, body):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} &mdash; NöraL</title>
  <link rel="icon" href="images/logo.jpg">
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
{NAV}
<div class="page-content">
{body}
</div>
{FOOTER}"""

pages = {}

pages['index.html'] = page('Home', """
<section class="hero">
  <div class="hero-inner">
    <div>
      <div class="hero-eyebrow"><span class="en">&#127941; Open Neuroscience Community</span><span class="tr">&#127941; A&#231;&#305;k N&#246;robilim Toplulu&#287;u</span></div>
      <h1><span class="en">Exploring the <span>Brain</span>, Building the Future</span><span class="tr">Beyni <span>ke&#351;fediyoruz</span>, gelece&#287;i in&#351;a ediyoruz</span></h1>
      <p class="hero-sub"><span class="en">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam.</span><span class="tr">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt. N&#246;robilim alan&#305;nda birlikte &#246;&#287;reniyoruz.</span></p>
      <div class="hero-actions">
        <a href="people.html" class="btn btn-primary"><span class="en">Meet the Team &rarr;</span><span class="tr">Ekibi Tan&#305; &rarr;</span></a>
        <a href="studies.html" class="btn btn-outline"><span class="en">Our Studies</span><span class="tr">&#199;al&#305;&#351;malar&#305;m&#305;z</span></a>
      </div>
    </div>
    <div class="hero-visual">
      <div class="brain-ring">
        <div class="ring ring-1"><div class="ring-dot"></div></div>
        <div class="ring ring-2"><div class="ring-dot"></div></div>
        <div class="ring ring-3"><div class="ring-dot"></div></div>
        <div class="brain-img"><img src="images/logo.jpg" alt="Brain"></div>
      </div>
    </div>
  </div>
</section>
<div class="stats-bar"><div class="stats-inner">
  <div><div class="stat-num" data-target="42" data-suffix="+">42+</div><div class="stat-label"><span class="en">Members</span><span class="tr">&#220;ye</span></div></div>
  <div><div class="stat-num" data-target="8">8</div><div class="stat-label"><span class="en">Active Projects</span><span class="tr">Aktif Proje</span></div></div>
  <div><div class="stat-num" data-target="15" data-suffix="+">15+</div><div class="stat-label"><span class="en">Publications</span><span class="tr">Yay&#305;n</span></div></div>
  <div><div class="stat-num" data-target="2024">2024</div><div class="stat-label"><span class="en">Founded</span><span class="tr">Kurulu&#351;</span></div></div>
</div></div>
<section class="bg-white"><div class="section-inner"><div class="about-split">
  <div class="about-img-wrap">&#129504;</div>
  <div>
    <span class="chip"><span class="en">About Us</span><span class="tr">Hakk&#305;m&#305;zda</span></span>
    <h2 class="section-title" style="margin-top:12px;"><span class="en">Who We Are</span><span class="tr">Biz Kimiz?</span></h2>
    <p style="color:var(--text-secondary);line-height:1.8;margin-bottom:20px;"><span class="en">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit.</span><span class="tr">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut enim ad minim veniam. Toplulu&#287;umuz n&#246;robilim severleri bir araya getirir.</span></p>
    <p style="color:var(--text-secondary);line-height:1.8;margin-bottom:28px;"><span class="en">Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit. We believe everyone can contribute to brain science.</span><span class="tr">Excepteur sint occaecat cupidatat non proident. Herkesin beyin bilimine katk&#305; yapabilece&#287;ine inan&#305;yoruz.</span></p>
    <a href="people.html" class="btn btn-dark"><span class="en">Meet the Team &rarr;</span><span class="tr">Ekiple Tan&#305;&#351; &rarr;</span></a>
  </div>
</div></div></section>
<section class="bg-light"><div class="section-inner">
  <div class="section-header center">
    <span class="chip"><span class="en">Latest</span><span class="tr">Son Haberler</span></span>
    <h2 class="section-title"><span class="en">News &amp; Updates</span><span class="tr">Haberler &amp; G&#252;ncellemeler</span></h2>
  </div>
  <div class="cards-grid">
    <div class="card"><div class="card-thumb">&#128225;</div><div class="card-body"><span class="card-chip"><span class="en">Event</span><span class="tr">Etkinlik</span></span><h3 class="card-title"><span class="en">Neuroscience Seminar: BCI</span><span class="tr">N&#246;robilim Semineri: BCI</span></h3><p class="card-text"><span class="en">Lorem ipsum dolor sit amet consectetur.</span><span class="tr">Lorem ipsum dolor sit amet consectetur.</span></p><span class="card-meta">15 June 2026</span></div></div>
    <div class="card"><div class="card-thumb">&#129516;</div><div class="card-body"><span class="card-chip"><span class="en">Research</span><span class="tr">Ara&#351;t&#305;rma</span></span><h3 class="card-title"><span class="en">New Project: Cognitive Load</span><span class="tr">Yeni Proje: Kognitif Y&#252;k</span></h3><p class="card-text"><span class="en">Lorem ipsum dolor sit amet consectetur.</span><span class="tr">Lorem ipsum dolor sit amet consectetur.</span></p><span class="card-meta">1 June 2026</span></div></div>
    <div class="card"><div class="card-thumb">&#128218;</div><div class="card-body"><span class="card-chip"><span class="en">Publication</span><span class="tr">Yay&#305;n</span></span><h3 class="card-title"><span class="en">Nature Neuroscience Translation</span><span class="tr">Nature Neuroscience &#199;evirisi</span></h3><p class="card-text"><span class="en">Lorem ipsum dolor sit amet consectetur.</span><span class="tr">Lorem ipsum dolor sit amet consectetur.</span></p><span class="card-meta">20 May 2026</span></div></div>
  </div>
  <div style="text-align:center;margin-top:36px;"><a href="news.html" class="btn btn-dark"><span class="en">All News &rarr;</span><span class="tr">T&#252;m Haberler &rarr;</span></a></div>
</div></section>
""" + CTA)

pages['people.html'] = page('People', """
<div class="page-hero"><div class="page-hero-content">
  <span class="chip"><span class="en">People</span><span class="tr">Ekip</span></span>
  <h1><span class="en">Meet the Team</span><span class="tr">Ekibimiz</span></h1>
  <p><span class="en">Lorem ipsum dolor sit amet. The minds behind NöraL.</span><span class="tr">Lorem ipsum dolor sit amet. NöraL'i olu&#351;turan insanlar.</span></p>
</div></div>
<section class="bg-white"><div class="section-inner">
  <div class="section-header center">
    <span class="chip"><span class="en">Founding Team</span><span class="tr">Kurucu Ekip</span></span>
    <h2 class="section-title"><span class="en">Leadership</span><span class="tr">Y&#246;netim</span></h2>
    <p class="section-sub"><span class="en">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</span><span class="tr">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</span></p>
  </div>
  <div class="team-grid">
    <div class="team-card"><div class="team-avatar">A</div><div class="team-name">Ad Soyad</div><div class="team-role"><span class="en">Founder &amp; President</span><span class="tr">Kurucu &amp; Ba&#351;kan</span></div><div class="team-bio"><span class="en">Lorem ipsum dolor sit amet. Neuroscience 3rd year, BCI research.</span><span class="tr">Lorem ipsum dolor sit amet. N&#246;robilim 3. s&#305;n&#305;f, BCI.</span></div><div class="team-links"><a href="#">in</a><a href="#">@</a></div></div>
    <div class="team-card"><div class="team-avatar">B</div><div class="team-name">Ad Soyad</div><div class="team-role"><span class="en">Research Coordinator</span><span class="tr">Ara&#351;t&#305;rma Koordinat&#246;r&#252;</span></div><div class="team-bio"><span class="en">Lorem ipsum dolor sit amet. Cognitive science and ML.</span><span class="tr">Lorem ipsum dolor sit amet. Kognitif bilim ve ML.</span></div><div class="team-links"><a href="#">in</a><a href="#">R</a></div></div>
    <div class="team-card"><div class="team-avatar">C</div><div class="team-name">Ad Soyad</div><div class="team-role"><span class="en">Events &amp; Communication</span><span class="tr">&#304;leti&#351;im &amp; Etkinlikler</span></div><div class="team-bio"><span class="en">Lorem ipsum dolor sit amet. Community management.</span><span class="tr">Lorem ipsum dolor sit amet. Topluluk y&#246;netimi.</span></div><div class="team-links"><a href="#">ig</a><a href="#">@</a></div></div>
    <div class="team-card"><div class="team-avatar">D</div><div class="team-name">Ad Soyad</div><div class="team-role"><span class="en">Publications Editor</span><span class="tr">Yay&#305;n Edit&#246;r&#252;</span></div><div class="team-bio"><span class="en">Lorem ipsum dolor sit amet. Blog and translations.</span><span class="tr">Lorem ipsum dolor sit amet. Blog ve &#231;eviriler.</span></div><div class="team-links"><a href="#">in</a></div></div>
    <div class="team-card"><div class="team-avatar">E</div><div class="team-name">Ad Soyad</div><div class="team-role"><span class="en">Technical Coordinator</span><span class="tr">Teknik Koordinat&#246;r</span></div><div class="team-bio"><span class="en">Lorem ipsum dolor sit amet. Data &amp; software. Python/MATLAB.</span><span class="tr">Lorem ipsum dolor sit amet. Veri &amp; yaz&#305;l&#305;m. Python/MATLAB.</span></div><div class="team-links"><a href="#">gh</a><a href="#">in</a></div></div>
    <div class="team-card"><div class="team-avatar">F</div><div class="team-name">Ad Soyad</div><div class="team-role"><span class="en">Academic Advisor</span><span class="tr">Akademik Dan&#305;&#351;man</span></div><div class="team-bio"><span class="en">Lorem ipsum dolor sit amet. Dr. &mdash; Neuroscience faculty.</span><span class="tr">Lorem ipsum dolor sit amet. Dr. &mdash; N&#246;robilim &#246;&#287;retim &#252;yesi.</span></div><div class="team-links"><a href="#">R</a><a href="#">@</a></div></div>
  </div>
</div></section>
<section class="bg-light"><div class="section-inner">
  <div class="section-header center">
    <span class="chip"><span class="en">Values</span><span class="tr">De&#287;erler</span></span>
    <h2 class="section-title"><span class="en">What We Stand For</span><span class="tr">Ne &#304;&#231;in Duruyoruz?</span></h2>
  </div>
  <div class="values-grid">
    <div class="value-card"><div class="value-icon">&#128275;</div><h3><span class="en">Open Science</span><span class="tr">A&#231;&#305;k Bilim</span></h3><p><span class="en">Lorem ipsum dolor sit amet, consectetur adipiscing.</span><span class="tr">Lorem ipsum dolor sit amet, consectetur adipiscing.</span></p></div>
    <div class="value-card"><div class="value-icon">&#127757;</div><h3><span class="en">Inclusivity</span><span class="tr">Kapsay&#305;c&#305;l&#305;k</span></h3><p><span class="en">Lorem ipsum dolor sit amet, consectetur adipiscing.</span><span class="tr">Lorem ipsum dolor sit amet, consectetur adipiscing.</span></p></div>
    <div class="value-card"><div class="value-icon">&#129309;</div><h3><span class="en">Collaboration</span><span class="tr">&#304;&#351;birli&#287;i</span></h3><p><span class="en">Lorem ipsum dolor sit amet, consectetur adipiscing.</span><span class="tr">Lorem ipsum dolor sit amet, consectetur adipiscing.</span></p></div>
    <div class="value-card"><div class="value-icon">&#128218;</div><h3><span class="en">Learning</span><span class="tr">S&#252;rekli &#214;&#287;renme</span></h3><p><span class="en">Lorem ipsum dolor sit amet, consectetur adipiscing.</span><span class="tr">Lorem ipsum dolor sit amet, consectetur adipiscing.</span></p></div>
    <div class="value-card"><div class="value-icon">&#9889;</div><h3><span class="en">Impact</span><span class="tr">Etki Odakl&#305;l&#305;k</span></h3><p><span class="en">Lorem ipsum dolor sit amet, consectetur adipiscing.</span><span class="tr">Lorem ipsum dolor sit amet, consectetur adipiscing.</span></p></div>
  </div>
</div></section>
""" + CTA)

pages['studies.html'] = page('Studies', """
<div class="page-hero"><div class="page-hero-content">
  <span class="chip"><span class="en">Research</span><span class="tr">Ara&#351;t&#305;rma</span></span>
  <h1><span class="en">Our Studies</span><span class="tr">&#199;al&#305;&#351;malar&#305;m&#305;z</span></h1>
  <p><span class="en">Lorem ipsum dolor sit amet. Active projects and academic publications.</span><span class="tr">Lorem ipsum dolor sit amet. Aktif projeler ve akademik yay&#305;nlar.</span></p>
</div></div>
<section class="bg-white"><div class="section-inner">
  <div class="section-header">
    <span class="chip"><span class="en">Active Projects</span><span class="tr">Aktif Projeler</span></span>
    <h2 class="section-title"><span class="en">Ongoing Research</span><span class="tr">Devam Eden &#199;al&#305;&#351;malar</span></h2>
  </div>
  <div class="cards-grid">
    <div class="card"><div class="card-thumb">&#129504;</div><div class="card-body"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;"><span class="card-chip">BCI</span><span class="badge badge-green"><span class="en">Active</span><span class="tr">Devam Ediyor</span></span></div><h3 class="card-title"><span class="en">EEG Motor Imagery Classification</span><span class="tr">EEG Motor G&#246;r&#252;nt&#252;leme S&#305;n&#305;fland&#305;rmas&#305;</span></h3><p class="card-text"><span class="en">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Deep learning classification of EEG signals.</span><span class="tr">Lorem ipsum dolor sit amet. EEG sinyallerinin derin &#246;&#287;renme ile s&#305;n&#305;fland&#305;r&#305;lmas&#305;.</span></p><div class="card-meta" style="margin-bottom:14px;"><span class="en">Lead: Ad Soyad &middot; 4 members</span><span class="tr">Sorumlu: Ad Soyad &middot; 4 ki&#351;i</span></div><a href="#" class="card-link"><span class="en">Details &rarr;</span><span class="tr">Detaylar &rarr;</span></a></div></div>
    <div class="card"><div class="card-thumb">&#128161;</div><div class="card-body"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;"><span class="card-chip">Cognitive</span><span class="badge badge-green"><span class="en">Active</span><span class="tr">Devam Ediyor</span></span></div><h3 class="card-title"><span class="en">Cognitive Load &amp; Learning Efficiency</span><span class="tr">Kognitif Y&#252;k ve &#214;&#287;renme Verimlili&#287;i</span></h3><p class="card-text"><span class="en">Lorem ipsum dolor sit amet. Measuring cognitive load using EEG and eye-tracking.</span><span class="tr">Lorem ipsum dolor sit amet. EEG ve g&#246;z izleme ile kognitif y&#252;k&#252; &#246;l&#231;me.</span></p><div class="card-meta" style="margin-bottom:14px;"><span class="en">Lead: Ad Soyad &middot; 5 members</span><span class="tr">Sorumlu: Ad Soyad &middot; 5 ki&#351;i</span></div><a href="#" class="card-link"><span class="en">Details &rarr;</span><span class="tr">Detaylar &rarr;</span></a></div></div>
    <div class="card"><div class="card-thumb">&#128300;</div><div class="card-body"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;"><span class="card-chip">AI+Neuro</span><span class="badge badge-yellow"><span class="en">Planned</span><span class="tr">Planlan&#305;yor</span></span></div><h3 class="card-title"><span class="en">Neural Network Dynamics Simulation</span><span class="tr">N&#246;ronal A&#287; Dinamikleri Sim&#252;lasyonu</span></h3><p class="card-text"><span class="en">Lorem ipsum dolor sit amet. Simulating biological neural networks with spiking models.</span><span class="tr">Lorem ipsum dolor sit amet. Biyolojik n&#246;ronal a&#287; davran&#305;&#351;lar&#305;n&#305; sim&#252;le etme.</span></p><div class="card-meta" style="margin-bottom:14px;"><span class="en">Lead: Ad Soyad &middot; 3 members</span><span class="tr">Sorumlu: Ad Soyad &middot; 3 ki&#351;i</span></div><a href="#" class="card-link"><span class="en">Details &rarr;</span><span class="tr">Detaylar &rarr;</span></a></div></div>
    <div class="card"><div class="card-thumb">&#128164;</div><div class="card-body"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;"><span class="card-chip">Neuroscience</span><span class="badge badge-green"><span class="en">Active</span><span class="tr">Devam Ediyor</span></span></div><h3 class="card-title"><span class="en">Sleep &amp; Memory Consolidation</span><span class="tr">Uyku S&#252;reci ve Bellek Konsolidasyonu</span></h3><p class="card-text"><span class="en">Lorem ipsum dolor sit amet. Investigating sleep stages and long-term memory formation.</span><span class="tr">Lorem ipsum dolor sit amet. Uyku a&#351;amalar&#305; ile bellek olu&#351;umu aras&#305;ndaki ili&#351;ki.</span></p><div class="card-meta" style="margin-bottom:14px;"><span class="en">Lead: Ad Soyad &middot; 4 members</span><span class="tr">Sorumlu: Ad Soyad &middot; 4 ki&#351;i</span></div><a href="#" class="card-link"><span class="en">Details &rarr;</span><span class="tr">Detaylar &rarr;</span></a></div></div>
  </div>
</div></section>
<section class="bg-light"><div class="section-inner">
  <div class="section-header">
    <span class="chip"><span class="en">Publications</span><span class="tr">Yay&#305;nlar</span></span>
    <h2 class="section-title"><span class="en">Academic Work</span><span class="tr">Akademik &#199;al&#305;&#351;malar</span></h2>
  </div>
  <div class="pub-filters">
    <button class="filter-btn active" data-filter="all"><span class="en">All</span><span class="tr">T&#252;m&#252;</span></button>
    <button class="filter-btn" data-filter="review"><span class="en">Review</span><span class="tr">Derleme</span></button>
    <button class="filter-btn" data-filter="translation"><span class="en">Translation</span><span class="tr">&#199;eviri</span></button>
    <button class="filter-btn" data-filter="blog">Blog</button>
    <button class="filter-btn" data-filter="poster"><span class="en">Poster</span><span class="tr">Sunum</span></button>
  </div>
  <div class="pub-list">
    <div class="pub-item" data-type="translation"><div class="pub-header"><div><span class="badge badge-blue" style="margin-bottom:8px;"><span class="en">Translation</span><span class="tr">&#199;eviri</span></span><h3 class="pub-title"><span class="en">Neuroplasticity &mdash; Nature Neuroscience Translation</span><span class="tr">N&#246;roplastisite &mdash; Nature Neuroscience &#199;evirisi</span></h3></div><span style="color:var(--text-secondary);font-size:.85rem;white-space:nowrap;">2025</span></div><p class="pub-meta"><span class="en">Translators: Ad Soyad, Ad Soyad &middot; May 2025</span><span class="tr">&#199;evirenler: Ad Soyad, Ad Soyad &middot; May&#305;s 2025</span></p><div class="pub-actions"><a href="#" class="pub-link"><span class="en">Read</span><span class="tr">Oku</span></a><a href="#" class="pub-link"><span class="en">Download</span><span class="tr">&#304;ndir</span></a></div></div>
    <div class="pub-item" data-type="review"><div class="pub-header"><div><span class="badge badge-green" style="margin-bottom:8px;"><span class="en">Review</span><span class="tr">Derleme</span></span><h3 class="pub-title"><span class="en">2020&ndash;2024 Neuroplasticity: Literature Review</span><span class="tr">2020&ndash;2024 N&#246;roplastisite Literat&#252;r Taramas&#305;</span></h3></div><span style="color:var(--text-secondary);font-size:.85rem;white-space:nowrap;">2024</span></div><p class="pub-meta"><span class="en">Authors: Ad Soyad, Ad Soyad &middot; December 2024</span><span class="tr">Yazarlar: Ad Soyad, Ad Soyad &middot; Aral&#305;k 2024</span></p><div class="pub-actions"><a href="#" class="pub-link"><span class="en">Read</span><span class="tr">Oku</span></a><a href="#" class="pub-link"><span class="en">Download</span><span class="tr">&#304;ndir</span></a></div></div>
    <div class="pub-item" data-type="blog"><div class="pub-header"><div><span class="badge" style="background:#FEE2E2;color:#991B1B;margin-bottom:8px;">Blog</span><h3 class="pub-title"><span class="en">Where are BCIs Headed? 2025 Perspective</span><span class="tr">BCI'lar Nereye Gidiyor? 2025 Perspektifi</span></h3></div><span style="color:var(--text-secondary);font-size:.85rem;white-space:nowrap;">2025</span></div><p class="pub-meta"><span class="en">Author: Ad Soyad &middot; February 2025</span><span class="tr">Yazar: Ad Soyad &middot; &#350;ubat 2025</span></p><div class="pub-actions"><a href="news.html" class="pub-link"><span class="en">Read</span><span class="tr">Oku</span></a></div></div>
    <div class="pub-item" data-type="poster"><div class="pub-header"><div><span class="badge badge-yellow" style="margin-bottom:8px;"><span class="en">Poster</span><span class="tr">Sunum</span></span><h3 class="pub-title"><span class="en">Attention Networks Pilot &mdash; Seminar</span><span class="tr">Dikkat A&#287;lar&#305; Pilot &mdash; Seminer</span></h3></div><span style="color:var(--text-secondary);font-size:.85rem;white-space:nowrap;">2025</span></div><p class="pub-meta"><span class="en">Presenter: Ad Soyad &middot; March 2025</span><span class="tr">Sunan: Ad Soyad &middot; Mart 2025</span></p><div class="pub-actions"><a href="#" class="pub-link"><span class="en">Slides</span><span class="tr">Slaytlar</span></a></div></div>
  </div>
</div></section>
""")

pages['news.html'] = page('News', """
<div class="page-hero"><div class="page-hero-content">
  <span class="chip"><span class="en">News</span><span class="tr">Haberler</span></span>
  <h1><span class="en">Latest Updates</span><span class="tr">G&#252;ncel Geli&#351;meler</span></h1>
  <p><span class="en">Lorem ipsum dolor sit amet. Events, lab news and highlights.</span><span class="tr">Lorem ipsum dolor sit amet. Etkinlikler ve &#246;ne &#231;&#305;kanlar.</span></p>
</div></div>
<section class="bg-white"><div class="section-inner">
  <div class="news-featured">
    <div>
      <span style="display:inline-block;background:rgba(0,207,201,.2);color:var(--c2);font-size:.75rem;font-weight:700;padding:4px 12px;border-radius:4px;text-transform:uppercase;letter-spacing:1px;margin-bottom:14px;"><span class="en">Featured</span><span class="tr">&#214;ne &#199;&#305;kan</span></span>
      <h2 style="font-family:'Sora',sans-serif;color:white;font-size:1.6rem;margin-bottom:12px;line-height:1.3;"><span class="en">Neuroscience Seminar: Brain-Computer Interfaces</span><span class="tr">N&#246;robilim Semineri: Beyin-Bilgisayar Aray&#252;zleri</span></h2>
      <p style="color:rgba(255,255,255,.72);line-height:1.75;margin-bottom:20px;font-size:.95rem;"><span class="en">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Join us to discuss BCI technologies and neuroscience research.</span><span class="tr">Lorem ipsum dolor sit amet. BCI teknolojilerini tart&#305;&#351;aca&#287;&#305;m&#305;z seminere davetlisiniz.</span></p>
      <div style="display:flex;align-items:center;gap:16px;flex-wrap:wrap;margin-bottom:20px;">
        <span style="color:rgba(255,255,255,.6);font-size:.85rem;">15 June 2026</span>
        <span style="color:rgba(255,255,255,.6);font-size:.85rem;">14:00</span>
        <span style="color:rgba(255,255,255,.6);font-size:.85rem;"><span class="en">Online / Campus</span><span class="tr">Online / Kamp&#252;s</span></span>
      </div>
      <a href="contact.html" class="btn btn-primary"><span class="en">Register &rarr;</span><span class="tr">Kay&#305;t Ol &rarr;</span></a>
    </div>
    <div class="news-featured-visual">&#129504;</div>
  </div>
  <div class="pub-filters" style="margin-bottom:36px;">
    <button class="filter-btn active" data-filter="all"><span class="en">All</span><span class="tr">T&#252;m&#252;</span></button>
    <button class="filter-btn" data-filter="event"><span class="en">Events</span><span class="tr">Etkinlik</span></button>
    <button class="filter-btn" data-filter="research"><span class="en">Research</span><span class="tr">Ara&#351;t&#305;rma</span></button>
    <button class="filter-btn" data-filter="lab">Lab</button>
    <button class="filter-btn" data-filter="team"><span class="en">Team</span><span class="tr">Ekip</span></button>
  </div>
  <div class="cards-grid">
    <div class="card" data-type="event"><div class="card-thumb">&#128225;</div><div class="card-body"><span class="card-chip"><span class="en">Event</span><span class="tr">Etkinlik</span></span><h3 class="card-title"><span class="en">Neuroscience Seminar: BCI</span><span class="tr">N&#246;robilim Semineri: BCI</span></h3><p class="card-text"><span class="en">Lorem ipsum dolor sit amet consectetur adipiscing.</span><span class="tr">Lorem ipsum dolor sit amet consectetur adipiscing.</span></p><div style="display:flex;justify-content:space-between;align-items:center;"><span class="card-meta">15 June 2026</span><a href="#" class="card-link"><span class="en">Read &rarr;</span><span class="tr">Devam&#305; &rarr;</span></a></div></div></div>
    <div class="card" data-type="research"><div class="card-thumb">&#129516;</div><div class="card-body"><span class="card-chip"><span class="en">Research</span><span class="tr">Ara&#351;t&#305;rma</span></span><h3 class="card-title"><span class="en">New Project: Cognitive Load</span><span class="tr">Yeni Proje: Kognitif Y&#252;k</span></h3><p class="card-text"><span class="en">Lorem ipsum dolor sit amet consectetur adipiscing.</span><span class="tr">Lorem ipsum dolor sit amet consectetur adipiscing.</span></p><div style="display:flex;justify-content:space-between;align-items:center;"><span class="card-meta">1 June 2026</span><a href="#" class="card-link"><span class="en">Read &rarr;</span><span class="tr">Devam&#305; &rarr;</span></a></div></div></div>
    <div class="card" data-type="research"><div class="card-thumb">&#128218;</div><div class="card-body"><span class="card-chip"><span class="en">Publication</span><span class="tr">Yay&#305;n</span></span><h3 class="card-title"><span class="en">Nature Neuroscience Translation Published</span><span class="tr">Nature Neuroscience &#199;evirisi Yay&#305;nda</span></h3><p class="card-text"><span class="en">Lorem ipsum dolor sit amet consectetur adipiscing.</span><span class="tr">Lorem ipsum dolor sit amet consectetur adipiscing.</span></p><div style="display:flex;justify-content:space-between;align-items:center;"><span class="card-meta">20 May 2026</span><a href="studies.html" class="card-link"><span class="en">Read &rarr;</span><span class="tr">Devam&#305; &rarr;</span></a></div></div></div>
    <div class="card" data-type="lab"><div class="card-thumb">&#128300;</div><div class="card-body"><span class="card-chip">Lab</span><h3 class="card-title"><span class="en">New EEG Device Joins the Lab</span><span class="tr">Yeni EEG Cihaz&#305; Laboratuvara Kat&#305;ld&#305;</span></h3><p class="card-text"><span class="en">Lorem ipsum dolor sit amet. 64-channel EEG boosts research capacity.</span><span class="tr">Lorem ipsum dolor sit amet. 64 kanall&#305; EEG cihaz&#305; ara&#351;t&#305;rma kapasitesini art&#305;r&#305;yor.</span></p><div style="display:flex;justify-content:space-between;align-items:center;"><span class="card-meta">10 May 2026</span><a href="#" class="card-link"><span class="en">Read &rarr;</span><span class="tr">Devam&#305; &rarr;</span></a></div></div></div>
    <div class="card" data-type="team"><div class="card-thumb">&#127942;</div><div class="card-body"><span class="card-chip"><span class="en">Team News</span><span class="tr">Ekip Haberi</span></span><h3 class="card-title"><span class="en">BCI Project Receives TUBITAK Grant</span><span class="tr">BCI Projemiz T&#220;B&#304;TAK Deste&#287;i Ald&#305;</span></h3><p class="card-text"><span class="en">Lorem ipsum dolor sit amet. EEG project awarded student support.</span><span class="tr">Lorem ipsum dolor sit amet. EEG projemiz T&#220;B&#304;TAK 2209-A deste&#287;i ald&#305;.</span></p><div style="display:flex;justify-content:space-between;align-items:center;"><span class="card-meta">15 March 2026</span><a href="#" class="card-link"><span class="en">Read &rarr;</span><span class="tr">Devam&#305; &rarr;</span></a></div></div></div>
    <div class="card" data-type="event"><div class="card-thumb">&#127908;</div><div class="card-body"><span class="card-chip"><span class="en">Event Report</span><span class="tr">Etkinlik Raporu</span></span><h3 class="card-title"><span class="en">Our First Seminar Was a Success</span><span class="tr">&#304;lk Seminerimiz B&#252;y&#252;k &#304;lgi G&#246;rd&#252;</span></h3><p class="card-text"><span class="en">Lorem ipsum dolor sit amet. Photos from our first seminar with 60+ attendees.</span><span class="tr">Lorem ipsum dolor sit amet. 60+ kat&#305;l&#305;mc&#305;n&#305;n yer ald&#305;&#287;&#305; ilk seminerimizden.</span></p><div style="display:flex;justify-content:space-between;align-items:center;"><span class="card-meta">5 March 2025</span><a href="#" class="card-link"><span class="en">Read &rarr;</span><span class="tr">Devam&#305; &rarr;</span></a></div></div></div>
  </div>
</div></section>
""")

pages['contact.html'] = page('Contact', """
<div class="page-hero"><div class="page-hero-content">
  <span class="chip"><span class="en">Contact</span><span class="tr">&#304;leti&#351;im</span></span>
  <h1><span class="en">Get in Touch</span><span class="tr">Bizimle &#304;leti&#351;ime Ge&#231;</span></h1>
  <p><span class="en">Lorem ipsum dolor sit amet. Questions, ideas or collaborations.</span><span class="tr">Lorem ipsum dolor sit amet. Sorular&#305;n, fikirlerin veya i&#351;birli&#287;i &#246;nerilerin.</span></p>
</div></div>
<section class="bg-light"><div class="section-inner">
  <div class="contact-grid">
    <div class="contact-info">
      <span class="chip"><span class="en">Contact Info</span><span class="tr">&#304;leti&#351;im Bilgileri</span></span>
      <h2 class="section-title" style="margin-top:12px;font-size:1.8rem;"><span class="en">Reach Us</span><span class="tr">Bize Ula&#351;</span></h2>
      <p><span class="en">Lorem ipsum dolor sit amet. We respond within 48 hours.</span><span class="tr">Lorem ipsum dolor sit amet. 48 saat i&#231;inde d&#246;n&#252;&#351; yap&#305;yoruz.</span></p>
      <div class="contact-detail"><div class="contact-detail-icon">&#128231;</div><div><div style="font-size:.8rem;color:var(--text-secondary);margin-bottom:2px;"><span class="en">Email</span><span class="tr">E-posta</span></div><a href="mailto:info@NöraL.com" style="color:var(--c1);font-weight:600;">info@NöraL.com</a></div></div>
      <div class="contact-detail"><div class="contact-detail-icon">&#127963;</div><div><div style="font-size:.8rem;color:var(--text-secondary);margin-bottom:2px;"><span class="en">Location</span><span class="tr">Konum</span></div><span style="font-weight:500;"><span class="en">University / Faculty Name</span><span class="tr">&#220;niversite / Fak&#252;lte Ad&#305;</span></span></div></div>
      <div style="margin-top:28px;"><div style="font-size:.85rem;font-weight:600;margin-bottom:14px;"><span class="en">Social Media</span><span class="tr">Sosyal Medya</span></div><div class="social-links"><a href="#" class="social-link">Instagram</a><a href="#" class="social-link">Twitter / X</a><a href="#" class="social-link">LinkedIn</a><a href="#" class="social-link">Telegram</a></div></div>
    </div>
    <div class="form-section">
      <div id="contact-success" class="success-msg"><span class="en">Message received! We will reply shortly.</span><span class="tr">Mesaj&#305;n al&#305;nd&#305;! En k&#305;sa s&#252;rede d&#246;n&#252;&#351; yapaca&#287;&#305;z.</span></div>
      <form id="contact-form">
        <div class="form-row">
          <div class="form-group"><label><span class="en">Name</span><span class="tr">Ad</span> <span>*</span></label><input type="text" placeholder="Lorem Ipsum" required></div>
          <div class="form-group"><label><span class="en">Email</span><span class="tr">E-posta</span> <span>*</span></label><input type="email" placeholder="lorem@ipsum.com" required></div>
        </div>
        <div class="form-group"><label><span class="en">Subject</span><span class="tr">Konu</span> <span>*</span></label><select required><option value="" disabled selected></option><option><span class="en">General Question</span><span class="tr">Genel Soru</span></option><option><span class="en">Collaboration</span><span class="tr">&#304;&#351;birli&#287;i</span></option><option><span class="en">Media</span><span class="tr">Medya</span></option><option><span class="en">Membership</span><span class="tr">&#220;yelik</span></option><option><span class="en">Other</span><span class="tr">Di&#287;er</span></option></select></div>
        <div class="form-group"><label><span class="en">Message</span><span class="tr">Mesaj</span> <span>*</span></label><textarea placeholder="Lorem ipsum dolor sit amet..." required style="min-height:140px;"></textarea></div>
        <div class="form-group"><div class="checkbox-group"><input type="checkbox" id="kvkk" required><label for="kvkk"><span class="en">I accept the <a href="#" style="color:var(--c2);">Privacy Policy</a>. (KVKK) <span style="color:#E94560;">*</span></span><span class="tr"><a href="#" style="color:var(--c2);">Gizlilik Politikas&#305;</a>'n&#305; kabul ediyorum. (KVKK) <span style="color:#E94560;">*</span></span></label></div></div>
        <button type="submit" class="btn btn-primary" style="width:100%;justify-content:center;font-size:1rem;padding:14px;"><span class="en">Send &rarr;</span><span class="tr">G&#246;nder &rarr;</span></button>
      </form>
    </div>
  </div>
</div></section>
""")

for name, content in pages.items():
    path = os.path.join(base, name)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Written: {name}  ({len(content):,} chars)')

for old in ['about.html','projects.html','publications.html','participate.html']:
    p = os.path.join(base, old)
    if os.path.exists(p):
        os.remove(p)
        print(f'Removed: {old}')

print('Done!')


