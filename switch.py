print('welcome rohit')
file = open('network.txt','r')

Name = file.readline().strip()
IOS = file.readline().strip()
Username = file.readline().strip()
Password = file.readline().strip()

print ('Hostname:', Name)
print ('IOS version:', IOS)
print ('Username:', Username)
print ('Password:', Password)