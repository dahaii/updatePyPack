import subprocess
import re

def get_outdated_packages():
    result = subprocess.run(['pip', 'list', '--outdated'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    lines = output.splitlines()
    outdated_packages = []
    for line in lines[2:]:  # İlk iki satır başlık bilgisi içerir
        parts = re.split(r'\s+', line)
        if len(parts) >= 4:
            outdated_packages.append(parts[0])
    return outdated_packages

def update_package(package):
    subprocess.run(['pip', 'install', '--upgrade', package])

def main():
    outdated_packages = get_outdated_packages()
    for package in outdated_packages:
        update_package(package)
        print(f'{package} güncellendi.')

if __name__ == '__main__':
    main()
