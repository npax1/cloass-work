
try:
    start = int(input("веди число і"))
    end = int(input("веди число"))
    sum=0
    counter=end-start+1
    for i in range(start, end+1):
        sum += i
        avg=sum/counter
    else:
        print(f'{sum}\n{avg}')
except Exception as ex:
    print(f"error information:{ex}")
finally:
    print("exit")

