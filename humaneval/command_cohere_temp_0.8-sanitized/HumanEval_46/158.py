def fib4(n: int):
    if n < 0:
        raise ValueError(" fib4 does not support negative indices")
    if n < 4:
        return n
    fib4_arr = [0, 0, 2, 0]
    for i in range(4, n+1):
        fib4_arr.append(fib4_arr[i-1] + fib4_arr[i-2] + fib4_arr[i-3] + fib4_arr[i-4])
    return fib4_arr[n]