def get_odd_collatz(n):
    odd_collatz_sequence = []
    num = n
    while num > 1:
        if num % 2 == 0:
            num = num // 2
        else:
            odd_collatz_sequence.append(num)
            num = 3 * num + 1
        if num % 2 != 0:
            break
    return odd_collatz_sequence