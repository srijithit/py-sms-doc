# app.py — IPL Auction Replica Event (Flask Web App)
# -------------------------------------------------
# Features included:
# ✔ Background video hero section
# ✔ Scroll animations (AOS)
# ✔ Mobile-first Instagram-style layout
# ✔ Live countdown timer
# ✔ Embedded Google Form registration
# ✔ Auction hammer sound + hover effects

from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
  <title>IPL Auction Replica Event | SNSCT</title>

  <!-- AOS Scroll Animation -->
  <link href=\"https://unpkg.com/aos@2.3.1/dist/aos.css\" rel=\"stylesheet\">

  <!-- Google Font -->
  <link href=\"https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;800&display=swap\" rel=\"stylesheet\">

  <style>
    body{margin:0;font-family:Poppins;background:#050814;color:#fff}

    /* HERO VIDEO */
    .hero{position:relative;height:100vh;overflow:hidden}
    .hero video{width:100%;height:100%;object-fit:cover}
    .overlay{position:absolute;inset:0;background:rgba(0,0,0,.65)}
    .hero-content{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:20px}

    h1{font-size:3.2rem;color:#f5c36a;text-shadow:0 0 25px #ffd98a}
    h2{font-weight:300;margin:10px 0 25px}

    .meta{display:flex;gap:15px;flex-wrap:wrap;justify-content:center}
    .meta div{background:rgba(255,255,255,.1);padding:10px 18px;border-radius:12px}

    .btn{margin-top:30px;padding:14px 36px;border:none;border-radius:40px;background:linear-gradient(90deg,#f5c36a,#ff9f1c);font-weight:700;cursor:pointer}

    section{padding:70px 8%}
    .grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:25px}
    .card{background:rgba(255,255,255,.06);padding:30px;border-radius:18px;backdrop-filter:blur(8px)}

    /* COUNTDOWN */
    .countdown{display:flex;justify-content:center;gap:25px;margin-top:30px}
    .time{background:#111;border-radius:14px;padding:20px;width:90px;text-align:center}
    .time h3{color:#f5c36a;margin:0}

    /* FOOTER */
    footer{text-align:center;padding:40px 20px;background:#02040c}
    footer h4{color:#f5c36a;letter-spacing:1px}

    @media(max-width:600px){
      h1{font-size:2.2rem}
      h2{font-size:1rem}
    }
  </style>
</head>
<body>

<!-- 🔥 HERO SECTION WITH VIDEO -->
<div class=\"hero\">
  <div class=\"overlay\"></div>
  <div class=\"hero-content\" data-aos=\"zoom-in\">
    <h1>IPL AUCTION</h1>
    <h2>Replica Event – Bid Smart. Build Legends. Rule the League.</h2>
    <div class=\"meta\">
      <div>📅 13.03.2026</div>
      <div>📍 SNSCT, Coimbatore</div>
      <div>⏰ 09:00 AM – 12:00 PM</div>
    </div>


    <!-- ⏳ COUNTDOWN TIMER -->
    <div class=\"countdown\" id=\"countdown\"></div>
  </div>
</div>

<!-- 📊 EVENT DETAILS -->
<section>
  <div class=\"grid\">
    <div class=\"card\" data-aos=\"fade-up\"><h3>Team Size</h3><p>4–6 Members</p></div>
    <div class=\"card\" data-aos=\"fade-up\"><h3>Virtual Purse</h3><p>₹50–100 Crores</p></div>
    <div class=\"card\" data-aos=\"fade-up\"><h3>Squad Size</h3><p>15–18 Players (Max 6 Overseas)</p></div>
  </div>
</section>

<!-- 📜 RULES SECTION -->
<section>
  <div class="grid">
    <div class="card" data-aos="fade-right">
      <h3>📜 Auction Rules</h3>
      <ul style="line-height:1.9; padding-left:18px">
        <li>Don’t exceed your purse 💸</li>
        <li>Follow overseas player limits 🌍</li>
        <li>No bids after <b>SOLD</b> 🔔</li>
        <li>Judges’ decision is final ⚖️</li>
      </ul>
    </div>
  </div>
</section>

<!-- 📩 REGISTRATION -->
<section id="register">
  <div class="card" data-aos="zoom-in" style="text-align:center">
    <h3>Registration</h3>
    <p>Click below to register for the IPL Auction Replica Event</p>
    <button class="btn" onclick="window.open('https://forms.gle/sybt5ksuUCcnYJ93A','_blank')">🚀 Register Now</button>
  </div>
</section>

<!-- 🔨 AUCTION SOUND -->
<audio id=\"hammer\" src=\"https://www.soundjay.com/misc/sounds/auction-hammer-1.mp3\"></audio>

<footer data-aos=\"fade-up\">
  <h4>STUDENT COORDINATORS</h4>
  <p>SRIJITH &nbsp; | &nbsp; POOJA</p>
  <p>📞 9791471277 &nbsp;</p>
</footer>

<!-- JS -->
<script src=\"https://unpkg.com/aos@2.3.1/dist/aos.js\"></script>
<script>
AOS.init();

// Countdown Timer
const eventDate = new Date('March 13, 2026 09:00:00').getTime();
setInterval(()=>{
  const now = new Date().getTime();
  const diff = eventDate - now;
  if(diff<0) return;
  const d=Math.floor(diff/(1000*60*60*24));
  const h=Math.floor((diff%(1000*60*60*24))/(1000*60*60));
  const m=Math.floor((diff%(1000*60*60))/(1000*60));
  document.getElementById('countdown').innerHTML = `
    <div class='time'><h3>${d}</h3><small>Days</small></div>
    <div class='time'><h3>${h}</h3><small>Hours</small></div>
    <div class='time'><h3>${m}</h3><small>Mins</small></div>`;
},1000);

// Hammer Sound on Button Hover
document.querySelectorAll('.btn').forEach(btn=>{
  btn.addEventListener('mouseenter',()=>document.getElementById('hammer').play());
});
</script>

</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML)

# 🏏 AUCTION SIMULATION DASHBOARD
@app.route("/dashboard")
def dashboard():
    return render_template_string(DASHBOARD_HTML)


def index():
    return render_template_string(HTML)

# ---------------- DASHBOARD HTML ----------------
DASHBOARD_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>IPL Auction Dashboard</title>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap" rel="stylesheet">
  <style>
    body{margin:0;font-family:Poppins;background:#050814;color:#fff}
    header{padding:25px;text-align:center;background:#02040c}
    header h1{color:#f5c36a;margin:0}
    .container{padding:40px 6%}
    .grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:25px}
    .card{background:rgba(255,255,255,.06);padding:25px;border-radius:18px}
    input,select,button{width:100%;padding:12px;margin-top:10px;border-radius:10px;border:none}
    button{background:linear-gradient(90deg,#f5c36a,#ff9f1c);font-weight:700;cursor:pointer}
    table{width:100%;border-collapse:collapse;margin-top:20px}
    th,td{padding:12px;text-align:center;border-bottom:1px solid #333}
    th{color:#f5c36a}
    .sold{color:#00ff9c;font-weight:700}
    .unsold{color:#ff5c5c;font-weight:700}
  </style>
</head>
<body>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)
    app.run(debug=True)
