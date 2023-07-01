import socket

def ip_to_domain(ip_address):
    try:
        domain = socket.gethostbyaddr(ip_address)[0]
        return domain
    except socket.herror:
        return "Tidak dapat menemukan domain untuk alamat IP tersebut."

def ip_to_domains_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            ips = file.readlines()
            ips = [ip.strip() for ip in ips]
            domains = [ip_to_domain(ip) for ip in ips]
            return domains
    except FileNotFoundError:
        return "File tidak ditemukan."
    except IOError:
        return "Terjadi kesalahan saat membaca file."

def save_to_file(data, file_path):
    try:
        with open(file_path, 'w') as file:
            for item in data:
                file.write(item + '\n')
        return "Data berhasil disimpan dalam file."
    except IOError:
        return "Terjadi kesalahan saat menyimpan file."
file_path = input("Masukkan file IP txt: ")
domains = ip_to_domains_from_file(file_path)
if isinstance(domains, list):
    print("Daftar domain:")
    for domain in domains:
        print(domain)

    domains_file_path = "domains.txt"
    save_result = save_to_file(domains, domains_file_path)
    print(save_result)
else:
    print(domains)
