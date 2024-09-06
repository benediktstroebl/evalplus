def get_odd_collatz(n):
    odd_collatz = []
    while n != 1:
        if n % 2 == 1:
            odd_collatz.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    odd_collatz.append(n)
    odd_collatz.sort()
    return odd_collatz