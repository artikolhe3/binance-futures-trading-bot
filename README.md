# Binance Futures Testnet Trading Bot

A simplified Python trading bot that places orders on **Binance Futures Testnet (USDT-M)** using a clean, reusable structure with proper logging and error handling.

This project was built as part of a technical application task.

---

## Features
- Place **MARKET** and **LIMIT** orders
- Supports **BUY** and **SELL**
- Command-line interface (CLI) using argparse
- Input validation and exception handling
- Structured project layout (client, orders, validators)
- Logs API requests, responses, and errors to a log file
- Uses Binance Futures **Testnet** only

---

## Tech Stack
- Python 3.x
- python-binance
- argparse
- logging

---

## Setup Instructions

### 1. Create Binance Futures Testnet Account
- Register at Binance Futures Testnet
- Generate API Key and Secret

### 2. Clone Repository
```bash
git clone <your-repo-url>
cd trading_bot
