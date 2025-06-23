# File: demo_builder.py
# ==============================================================================
# DEMO FILE UNTUK DESIGN PATTERN: BUILDER
# ==============================================================================

class Account:
    """
    Kelas Produk (Product). Ini adalah objek kompleks yang ingin kita buat.
    """
    def __init__(self, builder):
        self.nama = builder.nama
        self.email = builder.email
        self.nomor_telepon = builder.nomor_telepon
        self.alamat = builder.alamat
        self.saldo_poin = builder.saldo_poin

    def __str__(self):
        """Representasi string agar mudah dibaca saat dicetak."""
        info = (
            f"  - Nama          : {self.nama}\n"
            f"  - Email         : {self.email}\n"
            f"  - No. Telepon   : {self.nomor_telepon or 'Tidak diatur'}\n"
            f"  - Alamat        : {self.alamat or 'Tidak diatur'}\n"
            f"  - Saldo Poin    : {self.saldo_poin}"
        )
        return info

class AccountBuilder:
    """
    Kelas Builder. Menyediakan antarmuka yang jelas untuk
    membangun objek Account selangkah demi selangkah.
    """
    def __init__(self, nama: str, email: str):
        self.nama = nama
        self.email = email
        self.nomor_telepon = None
        self.alamat = None
        self.saldo_poin = 0

    def with_nomor_telepon(self, nomor_telepon: str):
        self.nomor_telepon = nomor_telepon
        return self

    def with_alamat(self, alamat: str):
        self.alamat = alamat
        return self

    def with_saldo_poin(self, poin: int):
        self.saldo_poin = poin
        return self

    def build(self) -> Account:
        return Account(self)


# ==============================================================================
# BAGIAN DEMONSTRASI
# ==============================================================================
if __name__ == "__main__":

    print("="*40)
    print("### DEMONSTRASI BUILDER PATTERN ###")
    print("="*40)

    print("\nLangkah 1: Membuat akun 'lengkap' dengan semua atribut opsional diisi.")
    akun_lengkap = (AccountBuilder("Dewi Lestari", "dewi@example.com")
                        .with_alamat("Jl. Cendrawasih No. 45, Jakarta")
                        .with_nomor_telepon("081211223344")
                        .with_saldo_poin(500)
                        .build())
    
    print("\n--- Hasil Akun Lengkap ---")
    print(akun_lengkap)
    
    print("\nLangkah 2: Membuat akun 'dasar' hanya dengan data wajib.")
    akun_dasar = AccountBuilder("Eko Prasetyo", "eko@example.com").build()

    print("\n--- Hasil Akun Dasar ---")
    print(akun_dasar)