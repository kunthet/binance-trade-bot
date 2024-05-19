
# Ubuntu 20.04

folder=binance1
pyenv=~/venv/binance

## To add ssh key on gcloud:
# gcloud compute os-login ssh-keys add \
#    --key-file=KEY_FILE_PATH \
#    --project=PROJECT \
#    --ttl=EXPIRE_TIME


sudo apt-get update --yes

# install Git
sudo apt-get install git-all --yes


# Python venv
sudo apt install python3-venv --yes
python3 -m venv $pyenv

# install PIP
#sudo apt-get install python3-pip --yes


folder=binance1
cd ~
mkdir ~/$folder
cd ~/$folder

# Clone repo
git clone https://github.com/kunthet/binance-trade-bot.git
cd binance-trade-bot
$pyenv/bin/pip3 install -r requirements.txt
echo "nohup $pyenv/bin/python3 -u -m binance_trade_bot &" > run.sh
chmod +x run.sh
chmod +x ./scripts/*.*