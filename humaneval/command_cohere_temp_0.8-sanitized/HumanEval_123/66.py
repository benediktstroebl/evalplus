def get_odd_collatz(n):
    odd_collatz = [1]
    while len(odd_collatz) < n:
        if len(odd_collatz) % 2 == 1:
            next_num = 3 * odd_collatz[-1] + 1
        else:
            next_num = odd_collatz[-1] // 2
        odd_collatz.append(next_num)
    return odd_collatz[:n]