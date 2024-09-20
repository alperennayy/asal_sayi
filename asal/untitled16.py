   #asal sayı mı değil mi #


try:
    a = int(input("Bir sayı giriniz: "))

    if a < 2:
        print(f"{a} sayısı asal değil.")
    else:
        i = 2
        while i < a:
            if a % i == 0:
                print(f"{a} sayısı asal değil.")
                break
            i = i + 1
        else:
            print(f"{a} sayısı asal.")
            
except ValueError:
    
    print("Lütfen geçerli bir sayı giriniz.")

    


