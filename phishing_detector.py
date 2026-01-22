import re

# List of common phishing keywords
PHISHING_KEYWORDS = [
    "urgent", "verify", "account suspended", "click here",
    "login immediately", "password", "bank", "security alert"
]

def detect_phishing(email_text):
    email_text = email_text.lower()
    score = 0

    # Keyword detection
    for word in PHISHING_KEYWORDS:
        if word in email_text:
            score += 1

    # URL detection
    urls = re.findall(r"http[s]?://\\S+", email_text)
    if urls:
        score += 2

    if score >= 3:
        return "⚠️ Phishing Email Detected"
    else:
        return "✅ Legitimate Email"

# Sample test emails
phishing_email = """
Dear User,
Your account has been suspended.
Click here immediately to verify your account:
http://fakebank-login.com
"""

legitimate_email = """
Hi Anuja,
Your meeting is scheduled for tomorrow at 10 AM.
Regards,
HR Team
"""

print("Phishing Email Result:", detect_phishing(phishing_email))
print("Legitimate Email Result:", detect_phishing(legitimate_email))

