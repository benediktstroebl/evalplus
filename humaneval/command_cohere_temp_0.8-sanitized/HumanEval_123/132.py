def get_odd_collatz(n):
    seq = [1]
    if n > 1:
        seq += [n]
        even = n
    while True:
        if seq[-1] % 2 == 0:
            even = int(seq[-1] / 2)
        else:
            even = 3 * seq[-1] + 1
        seq += [even]
        if even == 1:
            break
    return [x for x in seq if x % 2 != 0]