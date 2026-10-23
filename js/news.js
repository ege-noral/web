// News entries come from data/news.json. Empty arrays display an honest empty state.
(async () => {
  const container = document.querySelector('#home-news');
  if (!container) return;
  try {
    const response = await fetch('data/news.json');
    if (!response.ok) return;
    const data = await response.json();
    const items = Array.isArray(data.news) ? data.news.filter(n => n.date && n.title && n.published !== false) : [];
    items.sort((a,b) => b.date.localeCompare(a.date));
    if (!items.length) return;
    const list = document.createElement('div');
    list.className = 'updates-items';
    for (const n of items.slice(0,3)) {
      const row = document.createElement('article');
      row.className = 'update-row';
      const date = document.createElement('time');
      date.dateTime = n.date; date.textContent = n.date;
      const body = document.createElement('div');
      const heading = document.createElement('h3');
      const english = document.createElement('span'); english.className='en'; english.textContent= n.title.en || '';
      const turkish = document.createElement('span'); turkish.className='tr'; turkish.textContent= n.title.tr || n.title.en || '';
      heading.append(english,turkish); body.append(heading);
      if (n.category) {const tag=document.createElement('small'); tag.textContent=n.category; body.prepend(tag);}
      row.append(date,body);
      if (typeof n.url === 'string' && /^(https?:\/\/|[a-z0-9_-]+\.html(?:#[-a-z0-9_]+)?)$/i.test(n.url)) {
        const link=document.createElement('a'); link.href=n.url; link.textContent='↗'; link.setAttribute('aria-label','Read update'); row.append(link);
      }
      list.append(row);
    }
    container.replaceChildren(list);
  } catch (e) { /* Keep the visible empty state if opened locally or data is unavailable. */ }
})();
