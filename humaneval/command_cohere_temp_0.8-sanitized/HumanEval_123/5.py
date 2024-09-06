def get_odd_collatz(n):
    odd_collatz = [1]
    while n != 1: 
        if len(odd_collatz) == 0:
            return []
        if n % 2 == 0:
            n = n // 2
            odd_collatz.append(n)
        else:
            n = 3 * n + 1
            odd_collatz.append(n)
    return odd_collatz