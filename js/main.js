// ── Language toggle ─────────────────────────────────────────
(function () {
  const saved = localStorage.getItem('mw-lang') || 'en';
  document.body.classList.add('lang-' + saved);
  const btn = document.getElementById('lang-toggle');
  if (btn) {
    btn.textContent = saved === 'en' ? 'TR' : 'EN';
    btn.addEventListener('click', () => {
      const isEn = document.body.classList.contains('lang-en');
      document.body.classList.toggle('lang-en', !isEn);
      document.body.classList.toggle('lang-tr', isEn);
      const next = isEn ? 'tr' : 'en';
      localStorage.setItem('mw-lang', next);
      btn.textContent = next === 'en' ? 'TR' : 'EN';
    });
  }
})();

// ── Hamburger ───────────────────────────────────────────────
const hamburger = document.querySelector('.hamburger');
const navLinks  = document.querySelector('.nav-links');
if (hamburger) {
  hamburger.addEventListener('click', () => {
    navLinks.classList.toggle('open');
    hamburger.classList.toggle('active');
  });
}
document.querySelectorAll('.nav-links a').forEach(link => {
  link.addEventListener('click', () => {
    navLinks && navLinks.classList.remove('open');
    hamburger && hamburger.classList.remove('active');
  });
});

// ── Active nav link ─────────────────────────────────────────
const currentPage = window.location.pathname.split('/').pop() || 'index.html';
document.querySelectorAll('.nav-links a').forEach(link => {
  const href = link.getAttribute('href');
  if (href === currentPage || (currentPage === '' && href === 'index.html'))
    link.classList.add('active');
});

// ── Counter animation ───────────────────────────────────────
function animateCounter(el) {
  const target = parseInt(el.dataset.target);
  const step = target / (1800 / 16);
  let current = 0;
  const timer = setInterval(() => {
    current += step;
    if (current >= target) {
      el.textContent = target + (el.dataset.suffix || '');
      clearInterval(timer);
    } else {
      el.textContent = Math.floor(current) + (el.dataset.suffix || '');
    }
  }, 16);
}
const counters = document.querySelectorAll('[data-target]');
if (counters.length) {
  const obs = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting && !e.target.dataset.animated) {
        e.target.dataset.animated = '1';
        animateCounter(e.target);
      }
    });
  }, { threshold: 0.5 });
  counters.forEach(c => obs.observe(c));
}

// ── Filters ─────────────────────────────────────────────────
document.querySelectorAll('.pub-filters').forEach(wrapper => {
  const btns  = wrapper.querySelectorAll('.filter-btn');
  const items = document.querySelectorAll('[data-type]');
  btns.forEach(btn => {
    btn.addEventListener('click', () => {
      btns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const f = btn.dataset.filter;
      items.forEach(item => {
        item.style.display = (f === 'all' || item.dataset.type === f) ? '' : 'none';
      });
    });
  });
});

// ── Forms ───────────────────────────────────────────────────
function handleForm(formId, successId) {
  const form = document.getElementById(formId);
  const msg  = document.getElementById(successId);
  if (!form) return;
  form.addEventListener('submit', e => {
    e.preventDefault();
    if (msg) { msg.classList.add('show'); form.reset(); }
  });
}
handleForm('contact-form',    'contact-success');
handleForm('participate-form','participate-success');
