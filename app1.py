from flask import Flask, render_template_string, jsonify

app = Flask(__name__)

# Bot data with colors for each bot
bots = [
    {
        "username": "@TAMPMAILOFFICIALBOT",
        "name": "Temp Mail Bot",
        "description": """Temporary email generator bot.
This bot allows you to create disposable emails instantly.
Use it to register on websites without exposing your real email.
Protect your privacy and avoid spam with temporary inboxes.
Check emails in real-time with /inbox command.
Supports multiple domains for temporary emails.
Delete emails after use to keep inbox clean.
Send emails from the temporary mailbox using /mail.
Perfect for signing up on forums, apps, and services.
No registration required to use the bot.
Works instantly on Telegram with /start.
Get help and see all commands with /help.
Safe and secure to use on any device.
Compatible with Android, iOS, and desktop Telegram.
Reliable and fast email delivery.
No ads or hidden tracking.
Use temporary email to test services quickly.
Ideal for developers and testers.
Maintain anonymity while communicating online.
Useful for free trial registrations.
Prevents spam in your main inbox.
Quick setup, easy to use, fully automated.""",
        "commands": ["/start", "/mail", "/inbox", "/help"],
        "color": "#00ffff"
    },
    {
        "username": "@FFLIKESENDINDBOT",
        "name": "FF Player Info & Like Bot",
        "description": """Free Fire Player info and automatic like system.
Retrieve Free Fire player UID information instantly.
Track statistics like kills, rank, and matches played.
Send likes automatically to other players with /like.
Check detailed profile stats with /info command.
Supports multiple UID inputs.
View historical performance data over time.
Get insights for guild performance and leaderboard.
Helps in improving gameplay strategies.
Set reminders for daily like sending.
Interactive and easy-to-use interface.
Provides quick access to player achievements.
See rank distribution and win rate.
Automates repetitive tasks in Free Fire.
No need to manually check profiles.
Fully integrated with Telegram chat.
Safe and reliable bot usage.
Works on Android, iOS, desktop Telegram.
Perfect for competitive players and streamers.
Includes tips for boosting rank effectively.
Get daily statistics with /stats command.
Detailed logs of actions performed by the bot.""",
        "commands": ["/uid", "/like", "/info", "/stats"],
        "color": "#ff0000"
    },
    {
        "username": "@TPCGUILDVIPBOT",
        "name": "TPC Guild FF Bot",
        "description": """Guild management and Free Fire tools.
Manage your guild members efficiently with /members.
Assign ranks, track performance, and organize events.
Send announcements to all members with /guild.
Check member activity logs and participation.
Monitor guild rankings and achievements.
Set up automatic reminders for events.
Coordinate tournaments and challenges.
Analyze guild statistics and growth over time.
Integrates with Free Fire player stats.
Supports large guilds with hundreds of members.
View rank distribution within the guild.
Get alerts for inactive or misbehaving members.
Improve coordination and team strategy.
Manage roles, permissions, and access.
Perfect for competitive gaming guilds.
Track daily contributions and performance points.
Secure management without exposing personal info.
Fully automated commands to save time.
Interactive and responsive interface.
Provides recommendations to optimize guild performance.
Helps in guild recruitment and member engagement.""",
        "commands": ["/guild", "/rank", "/join", "/members"],
        "color": "#00ff00"
    },
    {
        "username": "@group_guardbot",
        "name": "Group Guard Bot",
        "description": """Telegram group security and link protection bot.
Prevent spam messages in your group chat.
Automatically delete unauthorized links with /lock.
Allow trusted members to share links with /unlock.
Warn users for violating group rules with /warn.
Ban repeat offenders with /ban command.
Monitor messages in real-time for malicious content.
Prevent fake accounts from joining your group.
Check member activity and message history.
Receive daily reports about group security.
Set custom rules for link sharing and media.
Protect your group from phishing attempts.
Keep chat clean and organized.
Automate moderation tasks efficiently.
Works on large groups with hundreds or thousands of members.
Supports multiple admins with different permissions.
Secure and reliable operations.
Easy-to-use commands with step-by-step instructions.
Fully compatible with Telegram mobile and desktop.
Interactive dashboard for admins.
Ideal for gaming, community, and official groups.
Enhances group engagement by reducing spam.
Maintains high-quality group environment.""",
        "commands": ["/lock", "/unlock", "/ban", "/warn"],
        "color": "#ffff00"
    },
    {
        "username": "@SOCIAL_MEDIA_VDO_DOWNLOADBOT",
        "name": "Video Downloader Bot",
        "description": """Download videos from any social media link.
Supports Instagram, Facebook, Twitter, TikTok, YouTube, and more.
Simply paste the video link and get it instantly.
Choose different video qualities and formats with /formats.
No login required for any social media platform.
Download private or public videos securely.
Get video previews before downloading.
Supports multiple downloads simultaneously.
Store downloaded videos on your device or cloud.
Automates repetitive download tasks.
Easy-to-use commands with friendly instructions.
Works with short links and redirects.
Maintain original video quality and resolution.
Fast download speeds with minimal delay.
Compatible with Android, iOS, and desktop Telegram.
Keep track of downloaded videos easily.
No hidden ads or pop-ups.
Perfect for content creators and viewers.
Share downloaded videos with friends directly.
Save stories and reels with ease.
Check download history with /help command.""",
        "commands": ["/download", "/help", "/formats"],
        "color": "#ff6600"
    },
    {
        "username": "@TG_SessionStringv9Bot",
        "name": "Session String Bot",
        "description": """Telegram session string generator bot.
Create secure Telegram session strings with /gen.
Check validity of strings with /check.
Store and manage multiple sessions easily.
Secure encryption to protect your Telegram accounts.
Use for automation bots and scripts.
Supports multi-device session management.
Works safely without exposing personal data.
Quick generation of strings for developers.
Automate Telegram tasks with generated strings.
Integrates with Telegram API seamlessly.
Perfect for bot developers and tech enthusiasts.
Get session info including user ID and bot permissions.
Easily share session strings with trusted collaborators.
Reliable performance and fast response times.
No need to manually login repeatedly.
Easy command usage for beginners.
Detailed guidance provided within the bot.
Compatible with Python, Node.js, and other scripts.
Track session usage for security.
Useful for testing and development purposes.""",
        "commands": ["/gen", "/string", "/check"],
        "color": "#ff00ff"
    },
    {
        "username": "@ButteyQueenAssistantbot",
        "name": "Personal AI Assistant",
        "description": """Personal AI assistant bot for daily tasks.
Ask questions, get advice, and manage schedules.
Automate reminders, to-do lists, and notes.
Interact naturally with AI chatbot capabilities.
Integrate with other bots for seamless workflow.
Get AI-generated responses for learning and entertainment.
Manage personal information safely.
Receive notifications for important events.
Use AI to optimize productivity and tasks.
Track habits and provide insights.
Voice input and response supported.
Analyze data and provide recommendations.
Set custom commands for repetitive tasks.
Monitor tasks completion efficiently.
Supports multiple languages.
Works on Android, iOS, and desktop Telegram.
Provides step-by-step guides for commands.
Secure and private AI interactions.
Ideal for personal or professional use.
Enhances daily efficiency and organization.
Continuous learning for smarter responses.
Fun and interactive AI conversation experience.""",
        "commands": ["/ask", "/ai", "/task", "/reminder"],
        "color": "#00ffcc"
    }
]

# HTML Template
html_template = """
<!DOCTYPE html>
<html>
<head>
  <title>VIP Bot Panel</title>
  <style>
    body {
      background: linear-gradient(135deg,#0a0a0a,#1a1a2e);
      font-family: 'Arial Black', Arial, sans-serif;
      color: #00ffff;
      margin:0;
      padding:0;
      text-align:center;
    }
    .header {
      text-align:center;
      padding:60px 20px;
      background:#0a0a0a;
      box-shadow:0 0 50px cyan;
    }
    .header h1 {
      font-size: 3em;
      margin:0;
      color: #00ffff;
      text-shadow: 0 0 5px #00ffff, 0 0 10px #00ffff, 0 0 15px #ff00ff, 0 0 20px #ff00ff;
    }
    .header p {
      font-size:1.5em;
      color:#ffffff;
      text-shadow: 0 0 5px purple;
    }
    .bot-card {
      background:#0a0a0a;
      margin:50px auto;
      padding:50px;
      border-radius:35px;
      box-shadow:0 0 40px purple;
      max-width:1000px;
      transition:0.3s;
      text-align:left;
    }
    .bot-card:hover {
      transform: scale(1.05);
    }
    .bot-card h2 {
      font-size: 3em;
      margin-bottom: 20px;
      text-align:center;
      color: #00ff00;
      text-shadow: 0 0 25px #00ff00;
    }
    .bot-card p {
      font-size: 1.7em;
      line-height:1.6em;
      margin: 10px 0;
    }
    .bot-card a {
      text-decoration: none;
    }
    .command {
      background: #111111;
      padding: 15px 25px;
      margin: 10px 8px;
      display: inline-block;
      border-radius: 15px;
      font-family: monospace;
      font-size: 1.6em;
      color: #00ffff;
      box-shadow: 0 0 20px cyan;
    }
  </style>
</head>
<body>
  <div class="header">
    <h1>🤖 SEXTY TG VIP BOT COLLECTION</h1>
    <p>All Bot Details in Full Mega VIP Look</p>
  </div>

  {% for bot in bots %}
    <div class="bot-card">
      <h2>{{ bot.name }}</h2>
      <p><b>Username:</b> 
        <a href="https://t.me/{{ bot.username[1:] }}" target="_blank" style="color: {{ bot.color }};">
          {{ bot.username }}
        </a>
      </p>
      <p>{{ bot.description|replace('\n','<br>')|safe }}</p>
      <p><b>Commands:</b></p>
      {% for cmd in bot.commands %}
        <a href="https://t.me/{{ bot.username[1:] }}?start={{ cmd[1:] }}" target="_blank">
          <span class="command">{{ cmd }}</span>
        </a>
      {% endfor %}
    </div>
  {% endfor %}
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html_template, bots=bots)

@app.route("/api/bots")
def get_bots():
    return jsonify(bots)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)