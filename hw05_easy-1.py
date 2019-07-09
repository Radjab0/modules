import os
print('Ваша директория {}'.format(os.getcwd()))
def makedir(i):
    os.mkdir('{}'.format(i))
def removedir(i):
    os.rmdir('{}'.format(i))
def chdir(i):
    os.chdir(i)
for r in range(9):
    makedir('dir_{}'.format(r+1))
print(os.listdir())
for r in range(9):
    removedir('dir_{}'.format(r+1))