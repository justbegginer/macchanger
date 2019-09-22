import subprocess
import random

interface = "eth0"


class operations:
    def __init__(self):
        operation = input()
        if operation == "show":
            self.show()
        elif operation == "change":
            self.change_Mac()

    def show(self):
        mac = return_Mac()
        print(mac)

    def change_Mac(self):
        first_mac = return_Mac()
        subprocess.call(f"ifconfig {interface} down", shell=True)
        subprocess.call(f"ifconfig {interface} hw ether " + random_Mac(), shell=True)
        subprocess.call(f"ifconfig {interface}", shell=True)
        last_mac = return_Mac()
        return self.change_Mac() if last_mac == first_mac else 0
        # TODO if we have a error that mac_addres is incorrect the programm doesn't change mac and first_mac=last_mac


def random_Mac():
    list = []
    for i in range(6):
        list.append(str(random.randint(1, 99)))
    print(":".join(list))
    return ":".join(list)
    # TODO fix this random mac


def return_Mac():
    ifconfig = str(subprocess.check_output("ifconfig "+interface, shell=True))
    part = ifconfig[ifconfig.index("ether") + 6:]  # mistype , subprocess.checkoutput() result is not a string
    mac_adress = ""
    for i in part:
        if i == " ":
            break
        else:
            mac_adress += i
    return mac_adress


def check_interface():
    ifconf_logs = str(subprocess.check_output("ifconfig", shell=True))
    return False if ifconf_logs.index(interface) == -1 else True


def main_func():
    print("choose interface (default is eth0)")
    interface = input()
    if not check_interface():
        print("error-invalid interface name")
        return
    print("choose operation")
    using = operations()


main_func()
