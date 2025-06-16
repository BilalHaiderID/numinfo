
# SIM Info Finder 🔍

A simple CLI tool to fetch PAK SIM owner details using mobile numbers or number ranges.
Uses `https://minahilsimsdata.info` as the data source.

---

## ✨ Features

- Fetch PAK SIM owner information by:
  - Single number
  - Multiple numbers (comma-separated)
  - Range of numbers (e.g., `03441234567-70`)
- Fast, clean CLI output
- Easy to extend and integrate

---

## 📦 Installation

```bash
git clone https://github.com/BilalHaiderID/numinfo
cd numinfo
pip install -r requirements.txt
```

> `requirements.txt` should contain:
```
requests
beautifulsoup4
```

---

## 🚀 Usage

### Single Number
```bash
python3 numinfo.py -n 03441234567
```

### Multiple Numbers
```bash
python3 numinfo.py -n 03441234567,03441234568,03441234569
```

### Number Range
```bash
python3 numinfo.py -r 03441234567-70
```

---

## 🛠 Example Output

```
[+] Number  : 03441234567
[+] Name    : Ahmed Ali
[+] CNIC    : 35202-1234567-1
[+] Address : Street 4, Lahore, Punjab
----------------------------------------
```

---

## 👨‍💻 Author

- **Name:** Bilal Haider ID
- **GitHub:** [github.com/BilalHaiderID](https://github.com/BilalHaiderID)



---

## ⚠️ Disclaimer
> This tool is intended for educational and legal use only.  
> The developer is not responsible for any misuse. Always obtain proper consent before querying personal data.

---

## 📜 License

MIT License — Use at your own risk.
