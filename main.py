import os
import shutil

def copy_files_with_extensions(src_folder, dest_folder, extensions):
    """
    Belirtilen uzantılara sahip dosyaları belirli bir klasörden hedef klasöre kopyalar.

    :param src_folder: Kaynak klasör
    :param dest_folder: Hedef klasör
    :param extensions: Kopyalanacak dosya uzantıları (örneğin: ['.jpg', '.png'])
    """
    # Hedef klasör yoksa oluştur
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # Kaynak klasördeki dosyaları gez
    for filename in os.listdir(src_folder):
        # Dosyanın tam yolu
        src_file_path = os.path.join(src_folder, filename)

        # Eğer bu bir dosya ise ve belirtilen uzantılardan birine sahipse
        if os.path.isfile(src_file_path) and any(filename.endswith(ext) for ext in extensions):
            # Hedef dosya yolunu belirle
            dest_file_path = os.path.join(dest_folder, filename)

            # Dosyayı kopyala
            shutil.copy2(src_file_path, dest_file_path)
            print(f"Kopyalandı: {src_file_path} -> {dest_file_path}")


for klasor_ad in  ['yolov8','donat','ehliyet','ehliyetDetection','KttSorguWs','qrRead','sftp_ehliyet_resimleri_al','yedekAl','kpsEhliyetWs']:

    src_directory = f'C:/Users/muhammet.sancaktutan/PycharmProjects/{klasor_ad}'  # Kaynak dizin yolu
    dest_directory = f'//10.10.10.176/Bereket Ortak/BT/muhammet/{klasor_ad}'   # Hedef dizin yolu
    file_extensions = ['.py','.yaml','txt']      # Kopyalanacak uzantılar

    copy_files_with_extensions(src_directory, dest_directory, file_extensions)
