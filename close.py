import subprocess
import pathlib


if __name__ == "__main__":
    PROC_NAMES_DIR = pathlib.Path(".").absolute()
    PROC_NAMES_FILENAME = "proc_names.txt"
    with open(PROC_NAMES_DIR / PROC_NAMES_FILENAME) as file:
        proc_names = file.read().split("\n")


    for proc_name in proc_names:
        subprocess.run("taskkill /im %s" % proc_name, shell=True, capture_output=False, text=None)