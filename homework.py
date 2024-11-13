'''


=== PROGRAM PAJAK ===

SEBUAH KOMPLEK MEMILIKI PROGRAM PAJAK BULANAN 
YANG MANA WARGA KOMPLEK WAJIB MEMBAYAR PAJAK 
SESUAI DENGAN PAJAK YANG SUDAH DITENTUKAN BERDASARKAN 
STATUS,PEKERJAAN,DAN GAJI YANG DIMILIKI OLEH 
SETIAP WARGA.

BUATLAH PROGRAM SEDERHANA UNTUK MENENTUKAN PAJAK 
YANG HARUS DI KELUARKAN TIAP-TIAP WARGA DAN JUGA 
BISA MEMERIKSA APAKAH SETIAP WARGA MEMBAYAR PAJAK
SESUAI DENGAN PAJAKNYA

=== PROGRAM HARUS MEMINTA INPUT ===

BERUPA :
>> NAMA 
>> STATUS
>> PEKERJAAN
>> GAJI

=== KRITERIA ===

>> KELAS 1 (PAJAK RP. 60.000)
GAJI >= 5.000.000/
PEKERJAAN = PNS,TNI,POLISI,DOKTER,PEGAWAI.

>> KELAS 2 (PAJAK RP. 30.000)
STATUS = SUDAH MENIKAH

>> KELAS 3 (PAJAK RP. 15.000)
SELAIN KRITERIA KELAS DI ATAS

SETELAH SEMUA DATA DI INPUT MAKA PROGRAM
AKAN MENCETAK PAJAK YANG HARUS DI BAYARKAN
DAN WARGA DIMINTA UNTUK MELAKUKAN PEMBAYARAN
DENGAN MENGINPUT NOMINAL SESUAI DENGAN KETENTUAN

JIKA PAJAK YNG DIBAYARKAN SESUAI DENGAN 
PAJAK YANG DITENTUKAN ATAU LEBIH MAKA PROGRAM AKAN
MENCETAK NAMA,PAJAK PERBULAN, STATUS PEMBAYARAN, 
DAN PESAN. JIKA TIDAK, PROGRAM AKAN MENCETAK PESAN
YANG SESUAI




'''


print()

import pyfiglet
fonts = ['xhelvb']
# for font in fonts :
#     print(f"\nFonts : {font}")


print(pyfiglet.figlet_format("      P A J A K", font='xhelvb'))
# fonts = pyfiglet.FigletFont.getFonts()
# print(fonts)

# result = pyfiglet.figlet_format("hallo")
# print(result)
print()
print("=====================================================================")
print('program "PAJAK" ini semata-mata untuk memperkaya diri "KETUA (AFIN)" dan semua warga WAJIB membayar pajak sesuai dengan ketentuan ')
print()
nama = str(input('MASUKAN NAMA ANDA : '))
status = str(input('MASUKAN STATUS ANDA : '))
pekerjaan = str(input('MASUKAN PEKERJAAN ANDA : '))
gaji = float(input('MASUKAN GAJI ANDA : '))
print()
print("============================= PEMBAYARAN ============================")
print()


status1 = ["SUDAH MENIKAH"]
pekerjaan1 = ["PNS","TNI","POLISI","DOKTER","PEGAWAI"]

a = (status  in status1)
b = ( pekerjaan  in  pekerjaan1)

kelas_a = ((gaji >= 5000000) or (pekerjaan in pekerjaan1) )

hasil = (kelas_a)
if (hasil == True):
    p = ('60.000')
    print(f'PAJAK YANG HARUS DI BAYAR : {p}')
    bayar = float(input('BAYAR :  '))
    if (bayar >= 60.000):
         pembayaran = ('LUNAS')
    else :
         pembayaran = ('GAGAL')
        

else :
     if  (status in status1) :
          p = ('30.000')
          print(f'PAJAK YANG HARUS DI BAYAR : {p}')
          bayar = float(input('BAYAR :  '))
          if (bayar >= 30.000):
               pembayaran = ('LUNAS')
          else :
               pembayaran = ('GAGAL')
            
         
     else :
          if (status not in status1):
               p = ('15.000')
               print(f'PAJAK YANG HARUS DI BAYAR : {p}')
               bayar = float(input('BAYAR :  '))
               if (bayar >= 15.000):
                     pembayaran = ('LUNAS')
               else:
                    pembayaran = ('GAGAL')
balas = ['LUNAS']
if (pembayaran in balas ):
     balasan = ('TERIMA KASIH SUDAH MEMPERKAYA DIRI KETUA')
else :
     balasan = ('ANDA DI HUKUM PENJARA AKIBAT TIDAK MEMBAYAR SESUAI PAJAK')

from colorama import Fore,Back,Style,init
from termcolor import colored
init()
print()
print("================================ CETAK ==============================")
print()
print(f'NAMA : {nama}')
print(f'PAJAK PERBBULAN : {p}')
print(f'STATUS PEMBAYARAN : {pembayaran}')
# print(Fore.RED + Back.WHITE + f'PESAN :  {balasan}')
print(colored(f'PESAN :  {balasan}', 'white', 'on_red'))
print()



# bayar = float(input('BAYAR : '))

# bayar1 = [bayar>=60.000]
# if ((True in bayar1 and ((bayar >= 60.000) == True)) or ((bayar >= 60.000) == True)):
#      q = ('pembayaran berhasil')
# else :
#      q = ('pembayaran gagal')

# print(q)
# print((bayar in bayar1 and ((bayar >= 60.000))))
# print(bayar in bayar1)
# print(bayar >= 60.000)
# print(bayar)
# print(bayar in bayar1 and ((bayar >= 60.000) == True))
# print([bayar>=60.000])




# hasil2 = (p)
# if (hasil2 == True):
#     p2 = ('30.000')
# else : 
#     p2 = kelas_c = (status not in status1)

# hasil_3 = (p2)
# if (hasil_3 == True):
#     p3 = ('15.000')
# else :
#     p3 = ("15.000")






       

