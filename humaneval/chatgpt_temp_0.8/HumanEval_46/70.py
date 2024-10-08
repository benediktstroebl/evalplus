def fib4(n: int):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        fib = [0, 0, 2, 0]
        for i in range(3, n+1):
            fib[i%4] = fib[(i-1)%4] + fib[(i-2)%4] + fib[(i-3)%4] + fib[(i-4)%4]
        return fib[n%4]
