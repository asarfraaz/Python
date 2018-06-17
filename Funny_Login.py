import random

def coding() :
    random_number = random.randint(1,25);

    print(random_number);
    i=0;
    j=0;
    while i<4 :
        passcode = input("Enter the passcode:");
        passcode = int(passcode);
        if random_number-passcode<-2 :
            print("invalid passcode");
        if random_number-passcode>2 :
            print("INVALID PASSCODE");
        if random_number-passcode<=2 and random_number-passcode!=0 and random_number-passcode>=-2 :
            print("InVaLiD PaSsCoDe");
            if j==0 :
                j=j+1
                i=i-1
        if random_number-passcode==0 :
            print("Welcome");
            break;
        i=i+1;
        if i==4 :
            print("Login failed");
            break;
        


def main() :
    coding();

main();
