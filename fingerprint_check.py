#Simple HTTPS certificate fingerprint verification

#SHA-256, SHA-1 fingerprints obtained via OpenSSL
openssl_fingerprint_SHA256 = "EE:2A:BF:62:44:01:30:40:1B:0E:5C:35:E3:B2:31:41:CE:F1:E6:2D:C6:A2:4C:F1:7B:2D:07:9E:82:87:79:BA"
openssl_fingerprint_SHA1 = "12:86:67:07:0A:5A:F4:32:5A:56:E5:2F:37:F6:FB:6B:68:11:E4:61"

#SHA-256, SHA-1 fingerprints obtained from browser certificate viewer
browser_fingerprint_SHA256 = "EE:2A:BF:62:44:01:30:40:1B:0E:5C:35:E3:B2:31:41:CE:F1:E6:2D:C6:A2:4C:F1:7B:2D:07:9E:82:87:79:BA"
browser_fingerprint_SHA1 = "12:86:67:07:0A:5A:F4:32:5A:56:E5:2F:37:F6:FB:6B:68:11:E4:61"

match_SHA1 = openssl_fingerprint_SHA1 == browser_fingerprint_SHA1
match_SHA256 = openssl_fingerprint_SHA256 == browser_fingerprint_SHA256

if match_SHA1 and  match_SHA256:
  print("Fingerprints match: True")
else:
  print("Fingerprints match: False")
  if not match_SHA1:
        print("Mismatch detected in SHA-1 fingerprint")
  if not match_SHA256:
        print("Mismatch detected in SHA-256 fingerprint")
