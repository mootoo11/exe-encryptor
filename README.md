
## English

### 📌 Purpose:
A tool to encrypt EXE files and convert them into encrypted DLLs, with an auto-generated script (`decrypt_stub.py`) for decrypting and temporarily running the original file.

---

### 🛠️ How It Works:
1. The user selects an EXE file.
2. The content is encrypted using symmetric encryption (Fernet – based on AES-128 + HMAC).
3. The encrypted file is saved as a `.dll`.
4. A decryption stub script (`decrypt_stub.py`) is generated to decrypt and run the file from a temporary location.
5. The user can supply a Base64 key or let the program generate one.

---

### 🔐 Encryption & Decryption:
- The EXE file is fully encrypted and unreadable without the key.
- The stub script:
  - Reads and decrypts the `.dll`.
  - Saves the result to a temp folder.
  - Runs it using `subprocess`.
  - Deletes the temp file after execution.

---

### 🛡️ Security Benefits:
- **Antivirus Evasion:** Encrypted files lack recognizable patterns or signatures.
- **Temporary Execution:** File runs only in memory and is deleted post-use.
- **Analysis Resistance:** When uploaded to tools like VirusTotal:
  - Encrypted file is unreadable.
  - Decryption stub looks harmless by itself unless combined with the encrypted file.

---

### 📦 Output Files:
- `output.dll`: The encrypted version of the original EXE.
- `decrypt_stub.py`: The decryption and execution stub.

---

### ✅ Requirements:
- Python 3
- `cryptography`
- tkinter (usually included with Python)

---

### 🔧 Installation
```bash
pip install -r requirements.txt
```

---
---


# 🔐 EXE Encryptor & Stub Generator

##  بالعربية

### 📌 الغرض الأساسي:
أداة لتشفير ملفات EXE وتحويلها إلى ملفات DLL مشفرة، مع إنشاء سكربت لفك التشفير والتشغيل لاحقًا. يهدف إلى حماية الملفات من التحليل الثابت ومحاولة تجاوز أنظمة الحماية.

---

### 🛠️ طريقة العمل:
1. يختار المستخدم ملف EXE المطلوب.
2. يتم تشفير الملف باستخدام تشفير متماثل (Fernet – مبني على AES-128 + HMAC).
3. يُحفظ الملف المشفر بصيغة DLL.
4. يتم إنشاء سكربت `decrypt_stub.py` يحتوي على كود فك التشفير وتشغيل الملف الأصلي مؤقتًا من مجلد مؤقت.
5. يمكن للمستخدم إدخال مفتاح تشفير مخصص (Base64) أو ترك البرنامج لتوليد مفتاح عشوائي.

---

### 🔐 التشفير وفك التشفير:
- يتم تشفير الملف بالكامل وتحويله إلى بيانات غير قابلة للقراءة.
- سكربت فك التشفير يقوم بـ:
  - فك تشفير DLL المشفر.
  - حفظ الملف المؤقت.
  - تشغيله باستخدام `subprocess`.
  - حذفه بعد الانتهاء.

---

### 🛡️ الفوائد الأمنية:
- **تخطي الفيروسات:** الملفات المشفرة لا تحتوي على توقيع معروف، ما يصعب كشفها.
- **تشغيل مؤقت وآمن:** الملف يعمل فقط في الذاكرة ولا يُترك على القرص بعد التنفيذ.
- **تحليل محدود عند الرفع على VirusTotal:** الملف المشفر لا يكشف محتواه، وسكربت فك التشفير بحد ذاته غير ضار بدون الملف المشفر.

---

### 📦 الملفات الناتجة:
- `output.dll`: الملف التنفيذي المشفر.
- `decrypt_stub.py`: سكربت فك التشفير وتشغيل الملف.

---

### ✅ المتطلبات:
- Python 3
- مكتبة `cryptography`
- tkinter (موجودة عادةً مع Python)

### 🔧 Installation
```bash
pip install -r requirements.txt
```
