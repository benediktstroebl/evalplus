def get_odd_collatz(n):
    seq = [1]
    if n > 1:
        seq += [n]
        odd_seq = [x for x in seq if x % 2 != 0]
    return odd_seq