import subprocess
import os
import ctypes
import platform

class EasyHub:
    def __init__(self):
        self.is_admin = self.check_admin()
        self.os_version = platform.system()
        self.is_windows = self.os_version == "Windows"

    def check_admin(self):
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    def optimize_network(self):
        if not self.is_windows:
            print("This program is designed to run on Windows devices only.")
            return

        if not self.is_admin:
            print("Please run this program as an administrator.")
            return

        self.adjust_tcp_settings()
        self.flush_dns()
        self.clear_temp_files()
        self.enable_firewall()

    def adjust_tcp_settings(self):
        print("Adjusting TCP settings for performance...")
        commands = [
            "netsh int tcp set global autotuninglevel=normal",
            "netsh int tcp set global rss=enabled"
        ]
        for command in commands:
            subprocess.run(command, shell=True)

    def flush_dns(self):
        print("Flushing DNS cache...")
        subprocess.run("ipconfig /flushdns", shell=True)

    def clear_temp_files(self):
        print("Clearing temporary files...")
        temp_folder = os.getenv('TEMP')
        try:
            for filename in os.listdir(temp_folder):
                file_path = os.path.join(temp_folder, filename)
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    os.rmdir(file_path)
        except Exception as e:
            print(f"An error occurred while clearing temporary files: {e}")

    def enable_firewall(self):
        print("Ensuring Windows Firewall is enabled...")
        subprocess.run("netsh advfirewall set allprofiles state on", shell=True)

if __name__ == "__main__":
    easy_hub = EasyHub()
    easy_hub.optimize_network()