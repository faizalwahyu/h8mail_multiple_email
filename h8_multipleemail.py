import subprocess

# Lokasi file yang berisi daftar email
email_file_path = 'emails.txt'

# Buka file output untuk menyimpan hasil
with open('output.txt', 'w') as output_file:
    # Buka file dan baca setiap baris (email)
    with open(email_file_path, 'r') as file:
        emails = file.readlines()

    # Jalankan h8mail untuk setiap email
    for email in emails:
        email = email.strip()  # Bersihkan whitespace atau newline
        command = [
            'h8mail',
            '-t', email
            # Tambahkan opsi lain yang dibutuhkan, misal '-c config_file.ini' jika menggunakan file konfigurasi
        ]
        # Eksekusi perintah
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Tulis output ke file dan tampilkan di terminal
        output = f"Results for {email}:\n{result.stdout}\nError (if any):\n{result.stderr}\n"
        output_file.write(output)
        print(output)
