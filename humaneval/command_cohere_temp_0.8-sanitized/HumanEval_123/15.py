def get_odd_collatz(n):
    odd_collatz_sequence = []
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        odd_collatz_sequence.append(n)
    return odd_collatz_sequence