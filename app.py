import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Valentine 💘", page_icon="💘", layout="centered")

if "page" not in st.session_state:
    st.session_state.page = "ask"

BG = "#ffd1dc"
CARD = "#ffe8ef"
BTN_YES = "#ff4d7d"
BTN_NO = "#ff6f96"
TEXT = "#222222"

def page_ask():
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
      <style>
        body {{
          margin:0;
          background:{BG};
          font-family: Poppins, Arial, sans-serif;
          display:flex;
          justify-content:center;
          padding:16px;
        }}

        .wrap {{
          width:100%;
          max-width:420px;
        }}

        .card {{
          background:{CARD};
          border-radius:22px;
          padding:18px 16px;
          box-shadow:0 10px 30px rgba(0,0,0,0.08);
          text-align:center;
        }}

        .imgbox {{
          display:flex;
          justify-content:center;
        }}
        .imgbox img {{
          width:88%;
          max-width:320px;
          border-radius:16px;
        }}

        h1 {{
          font-size:34px;
          font-weight:900;
          margin:14px 0 12px 0;
          color:{TEXT};
        }}

        .btnrow {{
          position:relative;
          height:90px;
          margin-top:10px;
          display:flex;
          justify-content:center;
          align-items:center;
          gap:16px;
        }}

        .yes {{
          background:{BTN_YES};
          color:white;
          border:none;
          border-radius:999px;
          padding:10px 28px;
          font-size:18px;
          font-weight:800;
          cursor:pointer;
          box-shadow:0 8px 18px rgba(255,92,138,0.35);
        }}

        .no {{
          position:absolute;
          left:55%;
          top:20px;
          background:{BTN_NO};
          color:white;
          border:none;
          border-radius:999px;
          padding:10px 28px;
          font-size:18px;
          font-weight:800;
          cursor:pointer;
          box-shadow:0 8px 18px rgba(255,127,163,0.35);
          transition:left 0.06s linear, top 0.06s linear;
        }}
      </style>
    </head>

    <body>
      <div class="wrap">
        <div class="card">
          <div class="imgbox">
            <img src="https://i.ibb.co/fx2nGqX/cute-bears-love.png" />
          </div>

          <h1>Do you love me?</h1>

          <div class="btnrow" id="btn-area">
            <button class="yes" onclick="sendYes()">Yes</button>
            <button class="no" id="no-btn">No</button>
          </div>
        </div>
      </div>

      <script>
        const noBtn = document.getElementById("no-btn");
        const area = document.getElementById("btn-area");

        function moveNo() {{
          const rect = area.getBoundingClientRect();
          const btnRect = noBtn.getBoundingClientRect();
          const step = 42;

          // up/down/opposite movement
          const moves = [
            {{dx:-step, dy:-step}},
            {{dx:+step, dy:+step}},
            {{dx:-step, dy:+step}},
            {{dx:+step, dy:-step}},
            {{dx:0, dy:-step*1.2}},
            {{dx:0, dy:+step*1.2}}
          ];
          const pick = moves[Math.floor(Math.random()*moves.length)];

          let left = parseFloat(noBtn.style.left || "55");
          let top  = parseFloat(noBtn.style.top  || "20");

          let leftPx = (left/100.0)*rect.width + pick.dx;
          let topPx  = top + pick.dy;

          if(leftPx < 0) leftPx = 6;
          if(leftPx > rect.width - btnRect.width) leftPx = rect.width - btnRect.width - 6;

          if(topPx < 0) topPx = 2;
          if(topPx > rect.height - btnRect.height) topPx = rect.height - btnRect.height - 2;

          noBtn.style.left = ((leftPx/rect.width)*100).toFixed(1) + "%";
          noBtn.style.top  = topPx.toFixed(0) + "px";
        }}

        noBtn.addEventListener("mouseenter", moveNo);
        noBtn.addEventListener("click", moveNo);
        noBtn.addEventListener("touchstart", moveNo);

        setInterval(()=>{{ if(Math.random()>0.55) moveNo(); }}, 250);

        function sendYes(){{
          // send message to streamlit
          window.parent.postMessage({{type:"YES_CLICKED"}}, "*");
        }}
      </script>
    </body>
    </html>
    """
    components.html(html, height=520)

def page_love():
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
      <style>
        body {{
          margin:0;
          background:{BG};
          font-family:Poppins, Arial, sans-serif;
          display:flex;
          justify-content:center;
          padding:16px;
        }}
        .wrap {{ width:100%; max-width:420px; }}
        .card {{
          background:{CARD};
          border-radius:22px;
          padding:18px 16px;
          box-shadow:0 10px 30px rgba(0,0,0,0.08);
          text-align:center;
        }}
        .heart {{
          width:64px;height:64px;background:#ff2f6d;
          position:relative;transform:rotate(45deg);
          animation:spin 1s linear infinite;
          border-radius:10px;
          margin:12px auto 10px auto;
        }}
        .heart:before,.heart:after {{
          content:""; width:64px;height:64px;background:#ff2f6d;
          border-radius:50%; position:absolute;
        }}
        .heart:before {{ top:-32px; left:0; }}
        .heart:after {{ left:-32px; top:0; }}
        @keyframes spin {{
          0% {{ transform:rotate(45deg) scale(1); }}
          50% {{ transform:rotate(225deg) scale(1.08); }}
          100% {{ transform:rotate(405deg) scale(1); }}
        }}
        img {{
          width:88%;
          max-width:320px;
          border-radius:16px;
        }}
        h1 {{
          font-size:34px;
          font-weight:900;
          margin:12px 0 0 0;
          color:{TEXT};
        }}
      </style>
    </head>
    <body>
      <div class="wrap">
        <div class="card">
          <div class="heart"></div>
          <img src="https://i.ibb.co/4t2h5mS/hug-bears.png" />
          <h1>I knew it 😍!</h1>
        </div>
      </div>
    </body>
    </html>
    """
    components.html(html, height=520)

# Listener for YES click
components.html(
    """
    <script>
    window.addEventListener("message", (event) => {
        if(event.data && event.data.type === "YES_CLICKED"){
            const url = new URL(window.parent.location);
            url.searchParams.set("love", "1");
            window.parent.location.href = url.toString();
        }
    });
    </script>
    """,
    height=0
)

# Routing
query = st.query_params
if "love" in query:
    st.session_state.page = "love"

if st.session_state.page == "ask":
    page_ask()
else:
    page_love()
            
