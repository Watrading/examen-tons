const SITE_OPEN = false; // Mets à false quand tu veux couper l’accès

window.onload = function() {
  if (!SITE_OPEN) {
    document.body.innerHTML = `
      <div style="margin-top:10em;text-align:center">
        <h2>Le site est actuellement fermé.</h2>
        <p>Merci de revenir plus tard.</p>
      </div>`;
  }
}
