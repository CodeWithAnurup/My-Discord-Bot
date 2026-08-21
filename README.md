# 🤖 My Discord Bot

A feature-rich Discord bot built with **discord.py v2**, hosted for free on **Render**.

## Features

| Feature | Details |
|---|---|
| 🔔 Welcome messages | Greets new members with an embed |
| 💬 Prefix commands | `!hello`, `!ping`, `!info`, `!userinfo`, `!kick`, `!ban`, `!clear` |
| ⚡ Slash commands | `/hello`, `/ping`, `/roll`, `/coinflip`, `/serverinfo`, `/avatar`, `/8ball` |
| 🌐 Keep-alive server | Built-in aiohttp web server for Render free tier |
| 🧩 Cog support | Modular command system via `cogs/` |

## Quick Start

```bash
# 1. Clone & enter the folder
git clone https://github.com/YOUR_USERNAME/my-discord-bot.git
cd my-discord-bot

# 2. Create virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up your token
copy .env.example .env        # Windows
# cp .env.example .env        # Mac/Linux
# Then edit .env and paste your bot token

# 5. Run
python bot.py
```

## Environment Variables

| Variable | Required | Description |
|---|---|---|
| `DISCORD_TOKEN` | ✅ | Your bot token from the Developer Portal |
| `SUPABASE_URL` | ❌ | Supabase project URL (if using DB) |
| `SUPABASE_KEY` | ❌ | Supabase anon key (if using DB) |

## Deployment (Render)

1. Push to GitHub
2. New Web Service → connect repo
3. **Build command**: `pip install -r requirements.txt`
4. **Start command**: `python bot.py`
5. Add `DISCORD_TOKEN` in Environment Variables
6. Set up [UptimeRobot](https://uptimerobot.com/) to ping your Render URL every 5 min

## Project Structure

```
my-discord-bot/
├── bot.py           ← main entry point (events + commands)
├── cogs/
│   └── general.py   ← example modular command group
├── .env             ← secrets (never commit!)
├── .env.example     ← template for collaborators
├── .gitignore
├── requirements.txt
└── README.md
```

## Commands Reference

### Prefix Commands (`!`)
| Command | Description |
|---|---|
| `!hello` | Bot greets you |
| `!ping` | Show latency |
| `!info` | Server info embed |
| `!userinfo [@user]` | User profile embed |
| `!clear [n]` | Delete n messages (needs Manage Messages) |
| `!kick @user [reason]` | Kick member (needs Kick Members) |
| `!ban @user [reason]` | Ban member (needs Ban Members) |

### Slash Commands (`/`)
| Command | Description |
|---|---|
| `/hello` | Bot greets you |
| `/ping` | Show latency |
| `/roll [sides]` | Roll a dice |
| `/coinflip` | Flip a coin |
| `/serverinfo` | Server info embed |
| `/avatar [@user]` | Show avatar |
| `/8ball <question>` | Magic 8-ball |

## Adding More Features

See `cogs/general.py` for an example of how to add commands in separate files. Load cogs in `bot.py` with:

```python
@bot.event
async def on_ready():
    await bot.load_extension("cogs.general")
    ...
```
