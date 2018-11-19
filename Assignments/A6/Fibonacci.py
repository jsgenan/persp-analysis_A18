def fib():
    first = 1
    second = 1
    index = 2
    while len(str(second))<1000:
        third = first+second
        first = second
        second = third
        index+=1
    return(index)

print(fib())