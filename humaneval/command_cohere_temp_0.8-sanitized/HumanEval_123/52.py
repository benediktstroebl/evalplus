def get_odd_collatz(n):
    seq = [1]
    if n > 1:
        seq += [n]
        odd = n
        even = n // 2
        while odd != 1 and even != 1:
            if odd % 2 == 1:
                odd = 3 * odd + 1
            else:
                even = (even // 2)
            seq += [odd, even]
        if odd != 1:
            seq += [odd]
    return sorted(set(seq) - {1})