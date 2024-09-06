def get_odd_collatz(n):
    seq = [1]
    if n > 1:
        seq += [n]
        even = n
        while even > 1:
            if len(seq) > 1000:
                break
            if even % 2 == 0:
                even //= 2
            else:
                even = 3 * even + 1
            if even % 2 != 0:
                seq += [even]
    return sorted(set(seq) - {1})