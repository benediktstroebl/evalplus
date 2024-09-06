def fib4(n: int) -> int:
    fib4_numbers = [0, 0, 2, 0]
    for i in range(5, n + 1):
        fib4_numbers.append(fib4_numbers[i - 1] + fib4_numbers[i - 2] + fib4_numbers[i - 3] + fib4_numbers[i - 4])
    return fib4_numbers[n]