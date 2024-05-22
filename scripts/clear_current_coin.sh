#!/bin/bash

# Execute the SQL command using sqlite3
sqlite3 -cmd '.timeout 1000' ../data/crypto_trading.db "DELETE FROM current_coin_history;"

echo "current coint cleared!"