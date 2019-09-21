#!/usr/bin/env python3

import datetime
import os
import shutil
import subprocess


##############---Переменные----###########
#Берем текущуюю дату
GetDate=datetime.datetime.now().strftime("%d-%m-%Y-(%H-%M-%S)")
#имя Бэкапа
Name_BackUP='Auto-BackUP'
#папка для бэкап-файлов
Dir_BackUP='filename'
#путь к подключенной флэшке
FLASH_DIR='/media/cashier/'
#белый
White='\033[1;98m'
#Красный цвет
RED='\033[1;31m'
#желтый цвет
YELLOW='\033[1;33m'
#голубой цвет
Cyan='\033[41;33;92m'
#конец цвета
Color_off='\033[0m'

########
list=os.listdir(FLASH_DIR)
#Проверка на наличие вставленой флешки,не более 1
if len(list) != 1:
    print('%s#############################################################%s' % (RED, Color_off))
    print('%s########%s----В СИСТЕМЕ НЕ ОБНАРУЖЕН FLASH-НАКОПИТЕЛЬ----%s######%s' % (RED, YELLOW, RED, Color_off))
    print('%s########%s----Или подключено больше одного НАКОПИТЕЛЯ----%s######%s' % (RED, YELLOW, RED, Color_off))
    print('%s########%s-----------Проверьте FLASH-НАКОПИТЕЛЬ----------%s######%s' % (RED, YELLOW, RED, Color_off))
    print('%s########%s-----------И перезапустите программу-----------%s######%s' % (RED, YELLOW, RED, Color_off))
    print('%s#############################################################%s' % (RED, Color_off))
#если вставлена 1, то продолжаем
else:
    tmp_flash_name = os.listdir('/media/cashier')
    Flash = FLASH_DIR + tmp_flash_name[0] + '/' + Name_BackUP + '/'
####
    ### входим в папку с бекапами на флешке
    ### создаем всплывающее окно запроса папки
    os.chdir(Flash)
    try:
        filename = subprocess.check_output(['zenity', '--file-selection', '--directory']).decode("utf-8").strip()
    except subprocess.CalledProcessError:
        pass

    # Переменные
    # папка для бэкап-файлов
    Dir_BackUP = filename
    # папка с торговой программой PSTrade
    PSTrade = '/home/cashier/.wine/drive_c/PSTrade'
    # папка  файлов фискалки
    FM1402 = '/home/cashier/.wine/drive_c/FM1402'
    # папка дисконтных карт
    DISCOUNT_Folder = '/home/cashier/.wine/drive_c/DiscountCard'
    # Cashmain.ini файл настроек торговли
    Cashmain_ini_file = '/home/cashier/.wine/drive_c/windows/CashMain.ini'
    # Cashmain из бэкапа
    Cashmain_ini = Dir_BackUP + '/CashMain.ini'
    # Cash.ini файл настрое пользователя и окон торговли
    Cash_ini_file = '/home/cashier/.wine/drive_c/windows/Cash.ini'
    # Cash.ini из бэкапа
    Cash_ini = Dir_BackUP + '/Cash.ini'
    # папка с сертификатами VPN
    VPN = '/etc/openvpn'
    # файл с настройками навесного оборудования
    Devices_file = '/etc/udev/rules.d/99-usb-serial.rules'
    # папуа файла навесного оборудования
    Devices_Backup = Dir_BackUP + '/99-usb-serial.rules'
    #
    Devices_Folder = '/etc/udev/rules.d/'
    # Reports из System32
    Reports = '/home/cashier/.wine/drive_c/windows/system32/Reports'
    # Берем текущуюю дату
    GetDate = datetime.datetime.now().strftime("%d-%m-%Y--%H-%M-%S")
    # имя Бэкапа
    Name_BackUP = 'Auto-BackUP'
    # папка для BackUP's
    BackUP = '%s%s' % (Flash, Dir_BackUP)
    # папка для BackUP's
    BackUP_PSTrade = Dir_BackUP + '/PSTrade'
    # папка для BackUP's
    BackUP_FM1402 = Dir_BackUP + '/FM1402'
    # папка для BackUP's
    BackUP_DISCOUNT_Folder = Dir_BackUP + '/DiscountCard'
    # папка для BackUP's
    BackUP_VPN = Dir_BackUP + '/openvpn/'
    # папка для BackUP's
    BackUP_Reports = Dir_BackUP + '/Reports'
    # файл ShopName
    Shop_Name_file = '/opt/ShopName.txt'
    #
    Shop_Name = Dir_BackUP + '/ShopName.txt'
    #opt
    Opt = '/opt'
    # BackUP-system32
    Sys32 = '/home/cashier/.wine/drive_c/windows/system32'
    # путь к подключенной флэшке
    FLASH_DIR = '/media/cashier/'
    # Диск C
    DriveC = '/home/cashier/.wine/drive_c/windows/'
    Error_TMP = '0'
########## DLL из System32
    AdmFrame = Dir_BackUP + '/Sys32/AdmFrame.dll'
    borlndmm = Dir_BackUP + '/Sys32/borlndmm.dll'
    Discount = Dir_BackUP + '/Sys32/Discount.dll'
    Weights = Dir_BackUP + '/Sys32/Weights.dll'
    PumpDLL = Dir_BackUP + '/Sys32/PumpDLL.dll'
    PsBackOffice = Dir_BackUP + '/Sys32/PsBackOffice.dll'
    AdmFrame_file = '/home/cashier/.wine/drive_c/windows/system32/AdmFrame.dll'
    borlndmm_file = '/home/cashier/.wine/drive_c/windows/system32/borlndmm.dll'
    Discount_file = '/home/cashier/.wine/drive_c/windows/system32/Discount.dll'
    Weights_file = '/home/cashier/.wine/drive_c/windows/system32/Weights.dll'
    PumpDLL_file = '/home/cashier/.wine/drive_c/windows/system32/PumpDLL.dll'
    PsBackOffice_file = '/home/cashier/.wine/drive_c/windows/system32/PsBackOffice.dll'

    # закрываем все программы
    os.system("sudo killall CashTerminal.exe")
    os.system("sudo killall RemoteModule.exe")
    os.system("sudo killall UnloadDiscountCard.exe")
    os.system("sudo killall dbsrv50.exe")
    os.system("sudo killall dbeng50.exe")
    os.system("sudo killall dbclient.exe")
    os.system("sudo killall OrdersClient.exe")
    print('%s################################################################################%s' % (RED, Color_off))

#функция копирования каталогов
    def copypath(SRC_PATH, DST_PATH):
        #проверка существования каталога в папке с бэкапом
        if not os.path.exists(SRC_PATH):
            global Error_TMP
            Error_TMP = int(Error_TMP) + 1
            #если не найдена выдаем соббщение
            TEXT = 'не найден'
            print('%s################################################################################%s' % (Cyan, Color_off))
            print('%s!!%s-%s-%s-%s!%s' % (Cyan, White, SRC_PATH, TEXT, Cyan, Color_off))
            print('%s################################################################################%s' % (Cyan, Color_off))
            return Error_TMP
        else:
            # проверка существования каталога в образе
            if not os.path.exists(DST_PATH):
                #если нет то копируем
                try:
                    shutil.copytree(SRC_PATH, DST_PATH)
                except Exception:
                    print('%s!!!!!%s--- ПРИ копировании %s произошла ошибка ---%s!!!!!%s' % (Cyan, White, SRC_PATH, Cyan, Color_off))
                    Error_TMP = int(Error_TMP) + 1
                    return Error_TMP
                else:
                    print('%s#%-9s-%s скопирован-%-9s#%s' % (RED, YELLOW, SRC_PATH, RED, Color_off))
                finally:
                    print('%s################################################################################%s' % (RED, Color_off))
            else:
                #если есть переименовываем старую,кладем новую
                os.rename(DST_PATH, DST_PATH + '-OLD-' + GetDate)
                try:
                    shutil.copytree(SRC_PATH, DST_PATH)
                except Exception:
                    print('%s!!!!!%s--- ПРИ копировании %s произошла ошибка ---%s!!!!!%s' % (Cyan, White, SRC_PATH, Cyan, Color_off))
                    Error_TMP = int(Error_TMP) + 1
                    return Error_TMP
                else:
                    print('%s#%-9s-%s скопирован-%-9s#%s' % (RED, YELLOW, SRC_PATH, RED, Color_off))
                finally:
                    print('%s################################################################################%s' % (RED, Color_off))

# функция копирования файлов
    def copydll(SRC_PATH, DST_PATH, NAME_FILE):
        # проверка существования каталога в папке с бэкапом
        if not os.path.exists(SRC_PATH):
            # если не найдена выдаем соббщение
            global Error_TMP
            Error_TMP = int(Error_TMP) + 1
            TEXT = 'не найден'
            print('%s################################################################################%s' % (Cyan, Color_off))
            print('%s!!%s-%s-%s-%s!%s' % (Cyan, White, SRC_PATH, TEXT, Cyan, Color_off))
            print('%s################################################################################%s' % (Cyan, Color_off))
            return Error_TMP
        else:
            # проверка существования файла в образе
            if not os.path.exists(NAME_FILE):
                # если нет то копируем
                try:
                    shutil.copy(SRC_PATH, DST_PATH)
                except Exception:
                    print('%s!!!!!%s--- ПРИ копировании %s произошла ошибка ---%s!!!!!%s' % (Cyan, White, SRC_PATH, Cyan, Color_off))
                    Error_TMP = int(Error_TMP) + 1
                    return Error_TMP
                else:
                    print('%s#%-9s-%s скопирован-%-9s#%s' % (RED, YELLOW, SRC_PATH, RED, Color_off))
                finally:
                    print('%s################################################################################%s' % (RED, Color_off))
            else:
                # если есть переименовываем старый,кладем новый
                os.rename(NAME_FILE, NAME_FILE + '-OLD-' + GetDate)
                try:
                    shutil.copy(SRC_PATH, DST_PATH)
                except Exception:
                    print('%s!!!!!%s--- ПРИ копировании %s произошла ошибка ---%s!!!!!%s' % (Cyan, White, SRC_PATH, Cyan, Color_off))
                    Error_TMP = int(Error_TMP) + 1
                    return Error_TMP
                else:
                    print('%s#%-9s-%s скопирован-%-9s#%s' % (RED, YELLOW, SRC_PATH, RED, Color_off))
                finally:
                    print('%s################################################################################%s' % (RED, Color_off))

# копируем файлы
    copypath(SRC_PATH=BackUP_FM1402, DST_PATH=FM1402)
    copypath(SRC_PATH=BackUP_PSTrade, DST_PATH=PSTrade)
    copypath(SRC_PATH=BackUP_DISCOUNT_Folder, DST_PATH=DISCOUNT_Folder)
    copypath(SRC_PATH=BackUP_Reports, DST_PATH=Reports)
    copydll(SRC_PATH=AdmFrame, DST_PATH=Sys32, NAME_FILE=AdmFrame_file)
    copydll(SRC_PATH=Discount, DST_PATH=Sys32, NAME_FILE=Discount_file)
    copydll(SRC_PATH=Weights, DST_PATH=Sys32, NAME_FILE=Weights_file)
    copydll(SRC_PATH=PumpDLL, DST_PATH=Sys32, NAME_FILE=PumpDLL_file)
    copydll(SRC_PATH=borlndmm, DST_PATH=Sys32, NAME_FILE=borlndmm_file)
    copydll(SRC_PATH=PsBackOffice, DST_PATH=Sys32, NAME_FILE=PsBackOffice_file)
    copydll(SRC_PATH=Cash_ini, DST_PATH=DriveC, NAME_FILE=Cash_ini_file)
    copydll(SRC_PATH=Cashmain_ini, DST_PATH=DriveC, NAME_FILE=Cashmain_ini_file)

#проверяем сертификаты из оброза и копируем из бэкапа
    if not os.path.exists(VPN):
        print()
    else:
        proc_tmp = 'sudo mv %s %s-%s' % (VPN, VPN, GetDate)
        os.system(proc_tmp)

    if not os.path.exists(BackUP_VPN):
        # если не найдена выдаем соббщение
        TEXT = 'не найден'
        print('%s################################################################################%s' % (Cyan, Color_off))
        print('%s!!%s-%s-%s-%s!%s' % (Cyan, White, BackUP_VPN, TEXT, Cyan, Color_off))
        print('%s################################################################################%s' % (Cyan, Color_off))
        Error_TMP = int(Error_TMP) + 1
    else:
        proc_tmp = 'sudo cp -r %s %s' % (BackUP_VPN, VPN)
        try:
            os.system(proc_tmp)
        except Exception:
            print('%s!!!!!%s--- ПРИ копировании %s произошла ошибка ---%s!!!!!%s' % (Cyan, White, BackUP_VPN, Cyan, Color_off))
            Error_TMP = int(Error_TMP) + 1
        else:
            print('%s#%-9s-%s скопирован-%-9s#%s' % (RED, YELLOW, BackUP_VPN, RED, Color_off))
        finally:
            print('%s################################################################################%s' % (RED, Color_off))

    if not os.path.exists(Shop_Name):
        # если не найдена выдаем соббщение
        TEXT = 'не найден'
        print('%s################################################################################%s' % (Cyan, Color_off))
        print('%s!!%s-%s-%s-%s!%s' % (Cyan, White, Shop_Name, TEXT, Cyan, Color_off))
        print('%s################################################################################%s' % (Cyan, Color_off))
        Error_TMP = int(Error_TMP) + 1
    else:
        proc_tmp = 'sudo cp -r %s %s' % (Shop_Name, Opt)
        try:
            os.system(proc_tmp)
        except Exception:
            print('%s!!!!!%s--- ПРИ копировании %s произошла ошибка ---%s!!!!!%s' % (Cyan, White, Shop_Name, Cyan, Color_off))
            Error_TMP = int(Error_TMP) + 1
        else:
            print('%s#%-9s-%s скопирован-%-9s#%s' % (RED, YELLOW, Shop_Name, RED, Color_off))
        finally:
            print('%s################################################################################%s' % (RED, Color_off))

    if not os.path.exists(Devices_Backup):
        # если не найдена выдаем соббщение
        TEXT = 'не найден'
        print('%s################################################################################%s' % (Cyan, Color_off))
        print('%s!!%s-%s-%s-%s!%s' % (Cyan, White, Devices_Backup, TEXT, Cyan, Color_off))
        print('%s################################################################################%s' % (Cyan, Color_off))
        Error_TMP = int(Error_TMP) + 1
    else:
        proc_tmp = 'sudo cp -r %s %s' % (Devices_Backup, Devices_Folder)
        try:
            os.system(proc_tmp)
        except Exception:
            print('%s!!!!!%s--- ПРИ копировании %s произошла ошибка ---%s!!!!!%s' % (Cyan, White, Devices_Backup, Cyan, Color_off))
            Error_TMP = int(Error_TMP) + 1
        else:
            print('%s#%-9s-%s скопирован-%-9s#%s' % (RED, YELLOW, Devices_Backup, RED, Color_off))
        finally:
            print('%s################################################################################%s' % (RED, Color_off))

    if int(Error_TMP) != 0:
        print('%s################################################################################%s' % (RED, Color_off))
        print('%s!!!!!%-20s--- ПРИ копировании произошло %-2s ОШИБОК ---%-25s!!!!!%s' % (Cyan, White, Error_TMP, Cyan, Color_off))
        print('%s###%-23s----Проверьте протокол копирования----%-27s###%s' % (Cyan, White, Cyan, Color_off))
        print('%s################################################################################%s' % (RED, Color_off))
    else:
        print('%s################################################################################%s' % (RED, Color_off))
        print('%s##%-24s---- НЕОБХОДИМЫЕ ФАЙЛЫ СКОПИРОВАНЫ ----%-25s###%s' % (RED, YELLOW, RED, Color_off))
        print('%s##%-35s---- Ошибок-%s ----%-35s###%s' % (RED, YELLOW, Error_TMP, RED, Color_off))
        print('%s################################################################################%s' % (RED, Color_off))
