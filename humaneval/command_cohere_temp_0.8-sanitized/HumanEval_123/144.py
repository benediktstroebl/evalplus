def get_odd_collatz(n):
    odd_collatz_sequence = []
    num = n
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = 3 * num + 1
        odd_collatz_sequence.append(num)
    return odd_collatz_sequence