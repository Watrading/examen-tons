import os

def rename_files(folder):
    # Liste tous les fichiers et trie-les dans l'ordre alphabétique
    files = sorted(os.listdir(folder))
    count = 1
    for filename in files:
        # Ne renomme que les fichiers .wav (change si besoin)
        if filename.lower().endswith('.wav'):
            new_name = f"{count:04}.wav"
            src = os.path.join(folder, filename)
            dst = os.path.join(folder, new_name)
            os.rename(src, dst)
            print(f"{filename} -> {new_name}")
            count += 1

# Les dossiers à traiter
base_dir = r"D:\python_envs\base_env\01_audio_together\02_wav"
folders = ["01_mono", "02_2syl"]

for folder in folders:
    folder_path = os.path.join(base_dir, folder)
    rename_files(folder_path)


