# wordle-telnet

Wordle in Telnet

## セットアップ手順

前提: Python 3.10が`/usr/local/python310/`配下にインストールされている

```sh
$ git clone https://github.com/geek-space-hq/wordle-telnet.git /srv/wordle-telnet
$ cd /srv/wordle-telnet
$ mkdir var
$ python3 ./scripts/gen_corpus.py
# ln -s ./server/wordle-telnet.socket /etc/systemd/system/wordle-telnet.socket
# ln -s ./server/wordle-telnet@.service /etc/systemd/system/wordle-telnet@.service
# systemctl daemon-reload
# systemctl start wordle-telnet.service
# systemctl enable wordle-telnet.service
```
