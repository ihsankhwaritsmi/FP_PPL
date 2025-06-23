# File: demo_singleton.py
# ==============================================================================
# DEMO FILE UNTUK DESIGN PATTERN: SINGLETON
# ==============================================================================

class AccountControllerSingleton:
    """
    Kelas Controller yang mengimplementasikan pola Singleton.
    """
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        """
        Metode yang mengontrol proses pembuatan objek.
        """
        if cls._instance is None:
            print("Singleton: Instance belum ada, membuat instance baru...")
            cls._instance = super(AccountControllerSingleton, cls).__new__(cls)
        else:
            print("Singleton: Menggunakan instance yang sudah ada...")
        
        return cls._instance

    def __init__(self):
        """
        Metode untuk inisialisasi atribut. Dicegah berjalan lebih dari sekali.
        """
        if self._initialized:
            return
        
        print("Singleton: Melakukan inisialisasi awal (hanya sekali)...")
        self.account_list = []
        self._initialized = True
    
    def registrasi(self, nama: str):
        print(f"Controller: Mendaftarkan '{nama}'...")
        self.account_list.append(nama)
    
    def get_all_accounts(self) -> list:
        return self.account_list


# ==============================================================================
# BAGIAN DEMONSTRASI
# ==============================================================================
if __name__ == "__main__":

    print("="*40)
    print("### DEMONSTRASI SINGLETON PATTERN ###")
    print("="*40)

    print("\nLangkah 1: Membuat instance controller pertama (misalnya dari LoginPage)")
    controller1 = AccountControllerSingleton()
    controller1.registrasi("Budi Santoso")
    controller1.registrasi("Susi Susanti")
    
    print("\nLangkah 2: Membuat instance controller kedua (misalnya dari AdminDashboard)")
    controller2 = AccountControllerSingleton()
    controller2.registrasi("Anton Wijaya")
    
    print("\nLangkah 3: Verifikasi")
    print(f"ID objek controller1: {id(controller1)}")
    print(f"ID objek controller2: {id(controller2)}")
    print(f"Apakah controller1 dan controller2 adalah objek yang sama? -> {controller1 is controller2}")
    
    print("\nKarena keduanya adalah objek yang sama, datanya pun sinkron:")
    print(f"Daftar akun yang diakses dari controller1: {controller1.get_all_accounts()}")
    print(f"Daftar akun yang diakses dari controller2: {controller2.get_all_accounts()}")