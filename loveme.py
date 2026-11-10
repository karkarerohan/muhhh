import html
import streamlit as st
import streamlit.components.v1 as components

# 1. Page settings (must be the first Streamlit command)
st.set_page_config(page_title="For You ❤️", page_icon="💖", layout="centered")

# 2. Read her name from the link, e.g. ...streamlit.app/?name=Priya
raw_name = st.query_params.get("name", "My Love")
name = html.escape(raw_name)  # makes the name safe to put inside HTML

# 3. Big title
st.markdown(
    f"<h1 style='text-align:center; color:#e91e63;'>Hey {name} 💕</h1>",
    unsafe_allow_html=True,
)

# 4. The trending "Will you be mine?" game, written in HTML + JavaScript
GAME = """
<div id="box" style="position:relative; height:380px; border-radius:20px;
     background:linear-gradient(135deg,#ffe0ec,#ffc1d9); font-family:sans-serif;
     text-align:center; overflow:hidden;">

  <div id="msg" style="padding-top:30px;">
    <div style="font-size:70px;">🧸</div>
    <h2 style="color:#c2185b;">__NAME__, will you be mine? 🥺</h2>
  </div>

  <button id="yes" style="position:absolute; left:25%; top:250px; font-size:20px;
          padding:12px 28px; border:none; border-radius:30px;
          background:#e91e63; color:white; cursor:pointer;">Yes 💖</button>

  <button id="no" style="position:absolute; left:60%; top:250px; font-size:18px;
          padding:10px 22px; border:none; border-radius:30px;
          background:#9e9e9e; color:white; cursor:pointer;">No 💔</button>
</div>

<script>
  const box = document.getElementById("box");
  const yes = document.getElementById("yes");
  const no  = document.getElementById("no");
  const msg = document.getElementById("msg");
  let size = 20;

  function runAway(e) {
    if (e) e.preventDefault();
    const maxX = box.clientWidth  - no.offsetWidth  - 10;
    const maxY = box.clientHeight - no.offsetHeight - 10;
    no.style.left = Math.random() * maxX + "px";
    no.style.top  = (130 + Math.random() * (maxY - 130)) + "px";
    size += 5;
    yes.style.fontSize = size + "px";
    yes.style.padding = (size / 2) + "px " + size + "px";
  }
  no.addEventListener("mouseover", runAway);
  no.addEventListener("touchstart", runAway);
  no.addEventListener("click", runAway);

  yes.addEventListener("click", function () {
    yes.remove(); no.remove();
    msg.innerHTML = '<div style="font-size:80px;">🥰</div>' +
      '<h1 style="color:#c2185b;">Yayyy! I love you! 💞</h1>' +
      '<p style="color:#ad1457;">Screenshot this and send it to me 😘</p>';
    for (let i = 0; i < 40; i++) {
      const h = document.createElement("div");
      h.textContent = ["❤️","💖","💕","🌹"][i % 4];
      h.style.cssText = "position:absolute; top:-30px; font-size:28px; left:" +
        Math.random() * 95 + "%; transition:top " + (2 + Math.random() * 2) + "s linear;";
      box.appendChild(h);
      setTimeout(() => { h.style.top = "400px"; }, 50);
    }
  });
</script>
""".replace("__NAME__", name)

components.html(GAME, height=400)

# 5. A love meter
st.markdown("### Rate how much I love you 😏")
level = st.slider("Drag it!", 0, 100, 50)
if level < 100:
    st.info("Hmm, that's too low. Try 100 😤")
else:
    st.success("Correct! Infinity actually ♾️❤️")
    st.balloons()

# 6. A secret letter
if st.button("Open my secret letter 💌"):
    st.snow()
    st.markdown(
        f"""
**Dear {name},**

- You make my boring days feel special.
- Your smile fixes my worst mood.
- I'm so lucky I found you.

*Forever yours,*
**Rohan** 💘
"""
    )