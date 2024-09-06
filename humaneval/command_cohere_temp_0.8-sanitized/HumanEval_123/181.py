def get_odd_collatz(n):
    odd_seq = []
    num = n
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
        odd_seq.append(num)
    return odd_seq