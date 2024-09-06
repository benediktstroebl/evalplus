def get_odd_collatz(n):
    seq = [1]
    while len(seq) <= n:
        if seq[-1] % 2 == 0:
            seq.append(seq[-1] // 2)
        else:
            seq.append(3 * seq[-1] + 1)
    return [num for num in seq if num % 2 != 0]