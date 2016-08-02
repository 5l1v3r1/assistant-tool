# -*- coding:utf-8 -*- 
#使用方法，建立一个文件夹，然后把目标文件和此文件放在同一个目录下，该目录下只允许此文件以外一个Py文件
#暂时只支持py文件的附件为文件而不是目录的封装，有附件文件的封装总是会出点错，多试几次
#尽量不要中断程序，封装结果如果把英文名改成中文名可能无法运行
import os
import glob
import shutil
def UsePyinstaller(path,Pathfile,filenameext,filename):
    shutil.copy(Pathfile,'C:\\PyInstaller-3.1\\')
    os.chdir('C:\\PyInstaller-3.1\\')
    os.system('python pyinstaller.py -F --noconsole '+filenameext)
    os.remove(filenameext)
    shutil.copy('C:\\PyInstaller-3.1\\'+filename+os.sep+'dist'+os.sep+filename+'.exe',path)
    shutil.rmtree(filename)

def extrato(u,r):
    t='N'
    for i in xrange(0,len(u)):
        if os.path.exists('C:\\PyInstaller-3.1\\'+r[i])==True:
            while t!='Y':
                t=raw_input(">Pyinstaller\ has a file with the same name as "+r[i]+" Continue?Y").upper()
        shutil.copy(u[i],'C:\\PyInstaller-3.1\\')
        
def extradel(u,r):
    for i in xrange(0,len(r)):
        os.remove(r[i])

u=[]
r=[]
for fn in glob.glob(os.getcwd()+os.sep+'*'):
    if os.path.isdir(fn):
        continue
    else:
        goal=os.path.split(fn)
        if len(goal)!=2:
            continue
        else:
            f=goal[1].split('.')
            if len(f)!=2:
                continue
            else:
                if f[0]!='python-package' and f[1]=='py':
                    path=goal[0]
                    Pathfile=fn
                    filenameext=goal[1]
                    filename=f[0]
                else:
                    if f[0]!='python-package':
                        u.append(fn)
                        r.append(goal[1])
print u
print r
#raw_input(">Files above will be copied to pyinstaller root,any key is to continue:")
extrato(u,r)
UsePyinstaller(path,Pathfile,filenameext,filename)
extradel(u,r)                      
                    
