def get_odd_collatz(n):
    seq = [1]
    while len(seq) < 1000000: 
        if seq[-1] % 2 == 0:
            seq.append(seq[-1] // 2)
        else:
            seq.append(3 * seq[-1] + 1)
        if seq[-1] == 1:
            break
    return [x for x in seq if x % 2 != 0]