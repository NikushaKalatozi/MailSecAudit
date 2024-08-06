
# MailSecAudit

One time project to audit mail security protocols (SPF, DKIM, DMARC)


## Authors

- [@NikushaKalatozi](https://github.com/NikushaKalatozi/)






[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


## Installation

Download MailSecAudit

```bash
  wget https://github.com/NikushaKalatozi/MailSecAudit.git
  pip install dnspython
  cd MailSecAudit
  python3 spfdkimdmarc_checker.py domains.txt
```
    to provide Python code with a domain list, by default, you should use "domains.txt", but you can change it to anything.
