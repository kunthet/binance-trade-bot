from datetime import datetime, timedelta

from binance_trade_bot import backtest

if __name__ == "__main__":
    history = []
    for manager in backtest(datetime(2024, 5, 15), datetime.now() - timedelta(hours=7)):
        btc_value = manager.collate_coins("USDT")
        bridge_value = manager.collate_coins(manager.config.BRIDGE.symbol)
        history.append((btc_value, bridge_value))
        btc_diff = round((btc_value - history[0][0]) / history[0][0] * 100, 3)
        bridge_diff = round((bridge_value - history[0][1]) / history[0][1] * 100, 3)
        current_coin = manager.db.get_current_coin()
        current_coin = current_coin.symbol if current_coin else ""
        
        progress = "-----------------------------------\n"
        progress += f"Current Coint: {current_coin}\n"
        progress += f"TIME: {manager.datetime}\n" 
        progress += f"BALANCES: {manager.balances}\n"
        progress += f"BTC VALUE: {btc_value} ({btc_diff}%)\n" 
        progress += f"{manager.config.BRIDGE.symbol} VALUE: {bridge_value} ({bridge_diff}%)\n"
        progress += "-----------------------------------\n\n"

        print(progress)
        with open("./logs/backtest_progress.txt", 'a', encoding="UTF-8") as f:
            f.write(progress)
