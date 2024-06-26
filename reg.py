

import winreg as wrg
import subprocess

pt2,pt,path_history,keyA='','','',[]

def menu():
    global root
    global pt
    global pt2
    global path_history

    ch=0
    try :
        
        while(ch!=11):
            print("------------------------------------------------\n Current path=",path_trace(),"\n---------------------------------------------------")
            ch=int(input("\n MENU \n 1.READ_REGISTRY_ENTRY \n 2.ADD_REGISTRY_ENTRY \n 3.SET_ROOT_LOCATION (HKEY_LOCAL_MACHINE,HKEY_CURRENT_USER,..) \n 4.GOTO_ANY_PATH \n 5.CREATE_KEY \n 6.CREATE_VALUE \n 7.LIST_KEYS \n 8.LIST_VALUES \n 9.RESET_PATH (FOR DIFFERENT KEYS) \n 10.EXIT- Enter choice: "))
            if(ch==1):
                read_registry_entry()
            elif(ch==2):
                add_registry_entry()
            elif(ch==3):
                rootloc()
            elif(ch==4):
                cdpath()
            elif(ch==5):
                mkkey()
            elif(ch==6):
                mkvalue()
            elif(ch==7):
                lskey()
            elif(ch==8):
                lsval()
            elif(ch==9):
                reset_path()
            elif(ch==10):
                clskeys()
                print("PROGRAM EXITED")
                ch=11
            else:
                print("INVALID KEY")
                
    except Exception as e:
            print("ERROR",e)
            menu()
        
def path_trace():
    full_path=pt+":"+r"\\"+pt2
    return full_path


def read_registry_entry():
    cdpath()
    lskey()
    lsval()
    reset_path()

def add_registry_entry():
    cdpath()
    mkkey()
    mkvalue()
    reset_path()

    
    

def rootloc():
    global root
    global pt
    global sf
    root=''
    
    ch=0
    try:
        while(ch!=6):
                reset_path()
                ch=int(input("\n ROOT KEYS \n 1.HKEY_CLASSES_ROOT \n 2.HKEY_CURRENT_USER \n 3.HKEY_LOCAL_MACHINE \n 4.HKEY_USERS \n 5.HKEY_CURRENT_CONFIG\n 6.QUIT \n Enter choice: "))
                if(ch==1):
                    root=wrg.HKEY_CLASSES_ROOT
                    pt='HKEY_CLASSES_ROOT'
                    sf='HKCR'

                elif(ch==2):
                    root=wrg.HKEY_CURRENT_USER
                    pt='HKEY_CURRENT_USER'
                    sf='HKCU'

                elif(ch==3):
                    root=wrg.HKEY_LOCAL_MACHINE
                    pt='HKEY_LOCAL_MACHINE'
                    sf='HKLM'

                elif(ch==4):
                    root=wrg.HKEY_USERS
                    pt='HKEY_USERS'
                    sf='HKU'

                elif(ch==5):
                    root=wrg.HKEY_CURRENT_CONFIG
                    pt='HKEY_CURRENT_CONFIG'
                    sf='HKCC'
                elif(ch==6):
                    print("PROGRAM EXITED")
                    root=0

                else:
                    print("INVALID KEY")
                    root=0
                
                return root
    except Exception as e:
            print("ERROR",e)
    
def cdpath():
    global pt2
    global key
    global path_history
    global keyA
    global k
        
    try:
        if(key==''):
            print("\nPlease select a hive before proceeding...")
            rootloc()
            print("------------------------------------------------\n Current path=",path_trace(),"\n---------------------------------------------------")
    except NameError:
        print("\nPlease select a hive before proceeding...")
        rootloc()
        print("------------------------------------------------\n Current path=",path_trace(),"\n---------------------------------------------------")
  


    pa=str(input("Enter registry path or keyname (eg:SOFTWARE or SOFTWARE\\\\Classes): "))
    k=pa

    if(path_history):
        pa=path_history+r"\\"+pa
    else:
        pa=pa
    
    try:
        key=wrg.OpenKeyEx(root,pa)
        keyA.append(key)
        if(key):
            pt2=pa
            path_history=pt2  # update path_history



    except Exception as e:
        
        print("Error", e)

def mkkey():
    keyn=str(input("Enter key_name: "))
    path=path_trace()
    try:
        nk=wrg.CreateKey(key,keyn)
        if(nk):
            print(f"Successfully created key: {keyn}")
            try:
                qn=str(input("Do you want to add another key y(yes)/n(no)"))
                if(qn=='y'):
                    mkkey()
                else:
                    pass
            except ValueError:
                mkkey()

    except Exception as e:
        print("Error",e)
        
def lskey():
            
    qn=input("Do you want to show all the keys -y(yes)/n(no)/c(cancel)")
    if(qn==('y' or 'yes')):
        print('--------------------------\nKeys\n-------------------------')
        i=0
        t=True
        while t==True:
            try :
                    subkey=wrg.EnumKey(key, i)
                    print(subkey)
                    i+=1
            except OSError:
                t=False
        print('\n --------------------\nkeys-end\n------------------------------\n')

    elif(qn==('n' or 'no')):
        no=int(input("Enter no of result to be shown: "))
        print('--------------------------\nKeys\n-------------------------')
        try :
            for i in range(no):
                subkey=wrg.EnumKey(key, i)
                print(subkey)
        except OSError:
                print('\n --------------------\nkeys-end\n------------------------------\n')
    
    elif(qn==('c' or 'cancel')):
        pass
    
    else:
        print("Invalid-Key")
        lskey()
    
def lsval():

    qn=input("Do you want to show all the values -y(yes)/n(no)/c(cancel)")
    if(qn==('y' or 'yes')):
        print('--------------------------\nValues\n-------------------------')
        i=0
        t=True
        while t==True:
            try :
                    subkey=wrg.EnumValue(key, i)
                    print(subkey)
                    i+=1
            except OSError:
                t=False
        print('\n --------------------\nValues-end\n------------------------------\n')


    elif(qn==('n' or 'no')):
        no=int(input("Enter no of result to be shown: "))
        print('--------------------------\nValues\n-------------------------')
        try :
            for i in range(no):
                subkey=wrg.EnumValue(key, i)
                print(subkey)
        except OSError:
                print('\n --------------------Values-end------------------------------\n')

    elif(qn==('c' or 'cancel')):
        pass
    
    else:
        print("Invalid-Key")
        lsval()





def mkvalue():
    try:
        # osaccess()
        ch=int(input("Enter type of value: \n 1.STRING \n 2.BINARY \n 3.DWORD-32 \n 4.DWORD-64 \n 5.Multi-String \n 6.Expandable-String \n Enter choice: "))
        if(ch==1):
            # vt=wrg.REG_SZ
            dt='String'
            val=str(input("Enter String-value: "))
        elif ch==2:
            # vt=wrg.REG_BINARY
            val=str(input("Enter Binary-value: "))
            dt='Binary'
        elif ch==3:
            # vt=wrg.REG_DWORD
            val=int(input("Enter DWORD value: "))
            dt='DWord'
        elif ch==4:
            # vt=wrg.REG_QWORD
            val=int(input("Enter QWORD value: "))
            dt='QWord'
        elif ch==5:
            # vt=wrg.REG_MULTI_SZ
            val=str(input("Enter Multi-String: ")).split(',')
            dt='MultiString'
        elif ch==6:
            # vt=wrg.REG_EXPAND_SZ
            val=str(input("Enter Expandable-String: "))
            dt='ExpandString'

        else:
            print("INVALID KEY")

        if(val):
            
            vn=str(input("Enter name: "))
            # re=wrg.SetValueEx(key, vn, 0, vt, val)
            k = path_trace().replace(pt, sf)
            psh=f"""New-ItemProperty -Path "{k}" -Name "{vn}" -Value "{val}" -Type {dt} -Force"""
            re=subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-Command", psh])
            if(re):
                print("Value set successfully!")
        
    except Exception as e:
        print("Error:", e)

    
def reset_path():
    global full_path
    global pt
    global pt2
    global path_history
    global key
    clskeys()
    full_path=''
    pt=''
    pt2=''
    path_history=''
    key=''

# def cdback():
#     global pt2
#     global path_history
#     bck=path_history-k
#     try:
#         key=wrg.OpenKeyEx(root,bck)
#         if(key):
#             wrg.CloseKey(keyA(len(keyA)-1))
#             path_history=bck # update path_history


    # except Exception as e:
        
    #     print("Error", e)


def clskeys():
    if keyA:
        #print("keyA", keyA)
        for i in keyA:
            try:
                ck=wrg.CloseKey(i)
            except OSError as e:
                print("failed to close", i, "error code:", e)



menu() #MAIN_FUNCTION
