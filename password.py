def password_analyzer():
    print("   PASSWORD CHECKER   ")

    password = input("Masukkan password: ")
    
    length = len(password)
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    special_chars = "!@#$%^&*()-_=+[{]};:'\",<.>/?\\|`~"
    
    # daftar blacklist
    blacklist = ["password", "12345678", "admin123", "qwerty"]

    # pengecekan dengan loop
    for char in password:
        if 'A' <= char <= 'Z':
            has_upper = True
        elif 'a' <= char <= 'z':
            has_lower = True
        elif '0' <= char <= '9':
            has_digit = True
        elif char in special_chars:
            has_special = True

    # hitung skor
    score = 0
    feedback = []

    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        feedback.append("- Terlalu pendek (min 8 karakter)")

    if has_upper and has_lower:
        score += 1
    else:
        feedback.append("- Campurkan huruf besar & kecil")

    if has_digit:
        score += 1
    else:
        feedback.append("- Tambahkan angka")

    if has_special:
        score += 1
    else:
        feedback.append("- Tambahkan simbol (!@#$ dll)")
    
    # cek Blacklist
    is_blacklisted = False
    for word in blacklist:
        if word in password.lower():
            is_blacklisted = True
            break

    print("\n HASIL ANALISIS")
    
    if is_blacklisted:
        print("STATUS: Tidak Aman.")
        print("Alasan: Password mengandung kata pasaran yang mudah ditebak.")
    else:
        if score >= 5:
            print("STATUS: KUAT")
        elif score >= 3:
            print("STATUS: SEDANG")
        else:
            print("STATUS: LEMAH")

    if feedback and not is_blacklisted:
        print("\nSaran:")
        for tips in feedback:
            print(tips)

# Jalankan fungsi
password_analyzer()
