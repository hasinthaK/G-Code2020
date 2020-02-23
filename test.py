fread = open("a_example.txt", "r")
# print(fread.read())

librarylist = []

basicData = fread.readline()
line2 = fread.readline()

print(basicData[2])
print(line2)
print(basicData.strip().split())


for itme1 in range(int(basicData.strip().split()[1])):
    temp = [fread.readline().strip().split(), fread.readline().strip().split()]
    librarylist.append(temp)


print(librarylist)

signuplist = {}

for it2 in range(len(librarylist)):
    signuplist[it2] = librarylist[it2][0][1]

print(signuplist) 

sortedsignup = {k: v for k, v in sorted(signuplist.items(), key=lambda item: item[1])}

print(sortedsignup)
print(sortedsignup.keys())

fwrite = open("demofile2.txt", "w+")
fwrite.write(str(len(sortedsignup.keys())))
fwrite.write("\n")

remaing = int(basicData.strip().split()[2])

for it33 in sortedsignup.keys():
    print(it33)
    days = int(len(librarylist[it33][1])/int(librarylist[it33][0][2]))
    # fwrite.write("\n")
    remaing = remaing-days-int(sortedsignup[it33])

    if(remaing<=10):
        break
    fwrite.write(str(it33)+" "+str(len(librarylist[it33][1])))
    
    fwrite.write("\n")
    for booklistsss in librarylist[it33][1]:
        fwrite.write(str(booklistsss)+" ")
    fwrite.write("\n")
   
    

    print(remaing)

   

fwrite.close()