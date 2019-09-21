#!/usr/bin/env python3

import datetime
import os
import shutil


#### Данный скрипт предназначен для безопасного копирования всех необходимых файлов перед заменой образа ####
#######################################
#######################################

# Переменные
###########
# папка с торговой программой PSTrade
PSTrade = '/home/cashier/.wine/drive_c/PSTrade'
# папка  файлов фискалки
FM1402 = '/home/cashier/.wine/drive_c/FM1402'
# папка дисконтных карт
DISCOUNT_Folder = '/home/cashier/.wine/drive_c/DiscountCard'
# Cashmain.ini файл настроек торговли
Cashmain_ini = '/home/cashier/.wine/drive_c/windows/CashMain.ini'
# Cash.ini файл настрое пользователя и окон торговли
Cash_ini = '/home/cashier/.wine/drive_c/windows/Cash.ini'
# папка с сертификатами VPN
VPN = '/etc/openvpn'
# файл с настройками навесного оборудования
Devices = '/etc/udev/rules.d/99-usb-serial.rules'
# Reports из System32
Reports = '/home/cashier/.wine/drive_c/windows/system32/Reports'
# Берем текущуюю дату
GetDate = datetime.datetime.now().strftime("%d-%m-%Y--%H-%M-%S")
# имя Бэкапа
Name_BackUP = 'Auto-BackUP'
# папка для бэкап-файлов
Dir_BackUP = '%s-%s' % (Name_BackUP, GetDate)
# папка для BackUP's
BackUP = '/home/cashier/.wine/drive_c/%s/%s' % (Name_BackUP, Dir_BackUP)
# папка для BackUP's
BackUP_PSTrade = '/home/cashier/.wine/drive_c/%s/%s/PSTrade/' % (
    Name_BackUP, Dir_BackUP)
# папка для BackUP's
BackUP_FM1402 = '/home/cashier/.wine/drive_c/%s/%s/FM1402/' % (
    Name_BackUP, Dir_BackUP)
# папка для BackUP's
BackUP_DISCOUNT_Folder = '/home/cashier/.wine/drive_c/%s/%s/DiscountCard/' % (
    Name_BackUP, Dir_BackUP)
# папка для BackUP's
BackUP_VPN = '/home/cashier/.wine/drive_c/%s/%s/openvpn/' % (
    Name_BackUP, Dir_BackUP)
# папка для BackUP's
BackUP_Reports = '/home/cashier/.wine/drive_c/%s/%s/Reports/' % (
    Name_BackUP, Dir_BackUP)
# папка для BackUP's
BackUP_Sys32 = '/home/cashier/.wine/drive_c/%s/%s/Sys32/' % (
    Name_BackUP, Dir_BackUP)
# файл ShopName
Shop_Name = '/opt/ShopName.txt'
# BackUP-system32
Sys32 = '/home/cashier/.wine/drive_c/%s/%s/Sys32' % (Name_BackUP, Dir_BackUP)
# путь к подключенной флэшке
FLASH_DIR = '/media/cashier/'
# Диск C
DriveC = '/home/cashier/.wine/drive_c/'
#
TMP_STR = '/home/cashier/.wine/drive_c/Auto-BackUP/'
# ifconfig
Ifconfig = '/home/cashier/.wine/drive_c/Auto-BackUP/ifconfig'
# переменная ошибок
Error_TMP = '0'


# белый
White = '\033[1;98m'
# Красный цвет
RED = '\033[1;31m'
# желтый цвет
YELLOW = '\033[1;33m'
# голубой цвет
Cyan = '\033[41;33;92m'
# конец цвета
Color_off = '\033[0m'
# DLL из System32
AdmFrame = '/home/cashier/.wine/drive_c/windows/system32/AdmFrame.dll'
borlndmm = '/home/cashier/.wine/drive_c/windows/system32/borlndmm.dll'
Discount = '/home/cashier/.wine/drive_c/windows/system32/Discount.dll'
Weights = '/home/cashier/.wine/drive_c/windows/system32/Weights.dll'
PumpDLL = '/home/cashier/.wine/drive_c/windows/system32/PumpDLL.dll'
PsBackOffice = '/home/cashier/.wine/drive_c/windows/system32/PsBackOffice.dll'

########
list = os.listdir(FLASH_DIR)
# print(len(list))
# Проверка на наличие вставленой флешки,не более 1
if len(list) != 1:
    print(
        '%s#############################################################%s' %
        (RED, Color_off))
    print(
        '%s########%s----В СИСТЕМЕ НЕ ОБНАРУЖЕН FLASH-НАКОПИТЕЛЬ----%s######%s' %
        (RED, YELLOW, RED, Color_off))
    print(
        '%s########%s----Или подключено больше одного НАКОПИТЕЛЯ----%s######%s' %
        (RED, YELLOW, RED, Color_off))
    print(
        '%s########%s-----------Проверьте FLASH-НАКОПИТЕЛЬ----------%s######%s' %
        (RED, YELLOW, RED, Color_off))
    print(
        '%s########%s------------ И перезапустите скрипт -----------%s######%s' %
        (RED, YELLOW, RED, Color_off))
    print(
        '%s#############################################################%s' %
        (RED, Color_off))
# если вставлена 1, то продолжаем
else:
    # если нет папки Auto-BackUP то создаем ее
    if not os.path.exists(DriveC + Name_BackUP):
        os.mkdir(DriveC + Name_BackUP)
    # Создаем в папке Auto-BackUP папку с датой
    os.mkdir(TMP_STR + Dir_BackUP)
    # закрываем все программы
    os.system("sudo killall CashTerminal.exe")
    os.system("sudo killall RemoteModule.exe")
    os.system("sudo killall UnloadDiscountCard.exe")
    os.system("sudo killall dbsrv50.exe")
    os.system("sudo killall dbeng50.exe")
    os.system("sudo killall dbclient.exe")
    os.system("sudo killall OrdersClient.exe")
    print(
        '%s################################################################################%s' %
        (RED, Color_off))
    print(
        '%s########%s-----------------------Торговое ПО отключено!--------------------%s#######%s' %
        (RED, YELLOW, RED, Color_off))
    print(
        '%s################################################################################%s' %
        (RED, Color_off))
    # Копируем все нужные файлы

    # функция копирования папки
    def copyFolder(SRC_PATH, DST_PATH):
        # если папки нет,даем сообщение
        if not os.path.exists(SRC_PATH):
            global Error_TMP
            Error_TMP = int(Error_TMP) + 1
            print(
                '%s################################################################################%s' %
                (Cyan, Color_off))
            print('%s!!!%s--%s не найден, скопируйте вручную--%s!!!%s' %
                  (Cyan, White, SRC_PATH, Cyan, Color_off))
            print(
                '%s################################################################################%s' %
                (Cyan, Color_off))
            return Error_TMP
        else:
            try:
                # если папка есть копируем
                shutil.copytree(SRC_PATH, DST_PATH)
            except Exception:
                print(
                    '%s!!%s ПРИ копировании %s произошла ошибка -%s!!%s' %
                    (Cyan, White, SRC_PATH, Cyan, Color_off))
                Error_TMP = int(Error_TMP) + 1
                return Error_TMP
            else:
                print(
                    '%s#%-10s-%s скопирован-%-10s#%s' %
                    (RED, YELLOW, SRC_PATH, RED, Color_off))
            finally:
                print(
                    '%s################################################################################%s' %
                    (RED, Color_off))

    # функция копирования file
    def copyFile(SRC_PATH, DST_PATH):
        # если file нет,даем сообщение
        if not os.path.exists(SRC_PATH):
            global Error_TMP
            Error_TMP = int(Error_TMP) + 1
            print(
                '%s################################################################################%s' %
                (Cyan, Color_off))
            print('%s!!!%s--%s не найден, скопируйте вручную--%s!!!%s' %
                  (Cyan, White, SRC_PATH, Cyan, Color_off))
            print(
                '%s################################################################################%s' %
                (Cyan, Color_off))
            return Error_TMP
        else:
            try:
                # если file есть копируем
                shutil.copy(SRC_PATH, DST_PATH)
            except Exception:
                Error_TMP = int(Error_TMP) + 1
                print(
                    '%s!!!!!%s--- ПРИ копировании %s произошла ошибка ---%s!!!!!%s' %
                    (Cyan, White, SRC_PATH, Cyan, Color_off))
                return Error_TMP
            else:
                print(
                    '%s#%-9s-%s скопирован-%-9s#%s' %
                    (RED, YELLOW, SRC_PATH, RED, Color_off))
            finally:
                print(
                    '%s################################################################################%s' %
                    (RED, Color_off))

    copyFolder(SRC_PATH=PSTrade, DST_PATH=BackUP_PSTrade)
    copyFolder(SRC_PATH=FM1402, DST_PATH=BackUP_FM1402)
    copyFolder(SRC_PATH=DISCOUNT_Folder, DST_PATH=BackUP_DISCOUNT_Folder)
    copyFolder(SRC_PATH=VPN, DST_PATH=BackUP_VPN)
    copyFolder(SRC_PATH=Reports, DST_PATH=BackUP_Reports)
    copyFile(SRC_PATH=Cashmain_ini, DST_PATH=BackUP)
    copyFile(SRC_PATH=Cash_ini, DST_PATH=BackUP)
    copyFile(SRC_PATH=Devices, DST_PATH=BackUP)
    copyFile(SRC_PATH=Shop_Name, DST_PATH=BackUP)

    # создаем папку для DLL и копируем их
    os.mkdir(BackUP_Sys32)
    copyFile(SRC_PATH=AdmFrame, DST_PATH=BackUP_Sys32)
    copyFile(SRC_PATH=borlndmm, DST_PATH=BackUP_Sys32)
    copyFile(SRC_PATH=Discount, DST_PATH=BackUP_Sys32)
    copyFile(SRC_PATH=Weights, DST_PATH=BackUP_Sys32)
    copyFile(SRC_PATH=PumpDLL, DST_PATH=BackUP_Sys32)
    copyFile(SRC_PATH=PsBackOffice, DST_PATH=BackUP_Sys32)

    os.system('ifconfig > /home/cashier/.wine/drive_c/Auto-BackUP/ifconfig')
    shutil.copy(Ifconfig, BackUP)
    print(
        '%-5s########%-10s---создан файл с ip-адресами----%-10s#######%-5s' %
        (RED, YELLOW, RED, Color_off))
    print(
        '%s################################################################################%s' %
        (RED, Color_off))
    # проверка на наличие авто-бэкап на флешке,если есть переименуем если нет копируем с диска С
    tmp_flash_name = os.listdir('/media/cashier')
    Flash = FLASH_DIR + tmp_flash_name[0] + '/' + Name_BackUP + '/'
    # если нет папки на флешке
    if not os.path.exists(FLASH_DIR + tmp_flash_name[0] + '/' + Name_BackUP):
        # создаем папку на флешке и копируем в нее
        os.mkdir(FLASH_DIR + tmp_flash_name[0] + '/' + Name_BackUP)
        try:
            shutil.copytree(BackUP, '%s%s' % (Flash, Dir_BackUP))
        except Exception:
            Error_TMP = int(Error_TMP) + 1
            print(
                '%s!!!!!%s--- ПРИ копировании %s на накопитель произошла ошибка ---%s!!!!!%s' %
                (Cyan, White, BackUP, Cyan, Color_off))
        else:
            if int(Error_TMP) != 0:
                print(
                    '%s################################################################################%s' %
                    (RED, Color_off))
                print(
                    '%s!!!!!%-20s--- ПРИ копировании произошло %-2s ОШИБОК ---%-25s!!!!!%s' %
                    (Cyan, White, Error_TMP, Cyan, Color_off))
                print(
                    '%s###%-23s----Проверьте протокол копирования----%-27s###%s' %
                    (Cyan, White, Cyan, Color_off))
                print(
                    '%s##%-25s------- файлы находятся в папках ------%-25s###%s' %
                    (RED, YELLOW, RED, Color_off))
                print(
                    '%s###%s-%s-%s###%s' %
                    (RED, YELLOW, BackUP, RED, Color_off))
                print(
                    '%s###%-20s------ и у вас на накопителе в папке --------%-23s###%s' %
                    (RED, YELLOW, RED, Color_off))
                print('%s###%s--%s%s---%s###%s' %
                      (RED, YELLOW, Flash, Dir_BackUP, RED, Color_off))
            else:
                print(
                    '%s################################################################################%s' %
                    (RED, Color_off))
                print(
                    '%s##%-24s---- НЕОБХОДИМЫЕ ФАЙЛЫ СКОПИРОВАНЫ ----%-25s###%s' %
                    (RED, YELLOW, RED, Color_off))
                print('%s##%-35---- Ошибок-%s ----%-35s###%s' %
                      (RED, YELLOW, Error_TMP, RED, Color_off))
                print(
                    '%s##%-25s------- они находится в папках -------%-25s###%s' %
                    (RED, YELLOW, RED, Color_off))
                print(
                    '%s##%s-%s-%s###%s' %
                    (RED, YELLOW, BackUP, RED, Color_off))
                print(
                    '%s##%-20s------ и у вас на накопителе в папке --------%-23s###%s' %
                    (RED, YELLOW, RED, Color_off))
                print('%s##%s--%s%s---%s###%s' %
                      (RED, YELLOW, Flash, Dir_BackUP, RED, Color_off))
        finally:
            print(
                '%s################################################################################%s' %
                (RED, Color_off))
# если на флешке есть папка для бэкапов
    else:
        try:
            shutil.copytree(BackUP, '%s%s' % (Flash, Dir_BackUP))
        except Exception:
            Error_TMP = int(Error_TMP) + 1
            print(
                '%s################################################################################%s' %
                (RED, Color_off))
            print(
                '%s!%s--- ПРИ копировании %s на накопитель произошла ошибка ---%s!%s' %
                (Cyan, White, BackUP, Cyan, Color_off))
        else:
            if int(Error_TMP) != 0:
                print(
                    '%s################################################################################%s' %
                    (RED, Color_off))
                print(
                    '%s!!!!!%-20s--- ПРИ копировании произошло %-2s ОШИБОК ---%-25s!!!!!%s' %
                    (Cyan, White, Error_TMP, Cyan, Color_off))
                print(
                    '%s###%-27s----Проверьте протокол копирования----%-27s###%s' %
                    (Cyan, White, Cyan, Color_off))
                print(
                    '%s##%-25s------- файлы находятся в папках ------%-25s###%s' %
                    (RED, YELLOW, RED, Color_off))
                print(
                    '%s###%s-%s-%s###%s' %
                    (RED, YELLOW, BackUP, RED, Color_off))
                print(
                    '%s###%-20s------ и у вас на накопителе в папке --------%-23s###%s' %
                    (RED, YELLOW, RED, Color_off))
                print('%s###%s--%s%s---%s###%s' %
                      (RED, YELLOW, Flash, Dir_BackUP, RED, Color_off))
            else:
                print(
                    '%s################################################################################%s' %
                    (RED, Color_off))
                print(
                    '%s##%-24s---- НЕОБХОДИМЫЕ ФАЙЛЫ СКОПИРОВАНЫ ----%-25s###%s' %
                    (RED, YELLOW, RED, Color_off))
                print('%s##%-35s---- Ошибок-%s ----%-35s###%s' %
                      (RED, YELLOW, Error_TMP, RED, Color_off))
                print(
                    '%s##%-25s------- они находится в папках -------%-25s###%s' %
                    (RED, YELLOW, RED, Color_off))
                print(
                    '%s##%s-%s-%s###%s' %
                    (RED, YELLOW, BackUP, RED, Color_off))
                print(
                    '%s##%-20s------ и у вас на накопителе в папке --------%-23s###%s' %
                    (RED, YELLOW, RED, Color_off))
                print('%s##%s--%s%s---%s###%s' %
                      (RED, YELLOW, Flash, Dir_BackUP, RED, Color_off))
        finally:
            print('%s################################################################################%s' % (RED, Color_off))


