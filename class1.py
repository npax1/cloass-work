try:
    number=int(input("numbeer->"))
    print(f"!{number}=", end="")
    temp=1
    for i in range(1,number+1):

        if i==number:
            print(i,end="")
        else:
            print(f'{i}+', end='')
        temp*=i
    print(f"={temp}")



except Exception as ex:
    print(f"error information:{ex}")
finally:
    print("exit")