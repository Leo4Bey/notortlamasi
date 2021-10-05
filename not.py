a=int(input("1. sınav notunuzu girin (0-100 arası)"))
b=int(input("2. sınav notunuzu girin (0-100 arası)"))
c=int(input("3. sınav notunuzu girin (0-100 arası)"))



if a>100 or a<0:
   
    print("Geçerli bir not giriniz")

if b>100 or b<0:

        print("Geçerli bir not giriniz")

if c>100 or c<0:

        print("Geçerli bir not giriniz")   

d=((a+b+c)/3)


if d>=90 and d<=100:

        print("AA") 
        print(d)

if d>=85 and d<=89:

        print("BA")   
        print(d)

if d>=80 and d<=84:

        print("BB")   
        print(d)

if d>=75 and d<=79:

        print("CB")   
        print(d)

if d>=70 and d<=74:

        print("CC")   
        print(d)

if d>=65 and d<=69:

        print("DC")   
        print(d)

if d>=60 and d<=64:

        print("DD")   
        print(d)

if d>=50 and d<=59:

        print("FD")   
        print(d)

if d>=0 and d<=49:

        print("FF")   
        print(d)