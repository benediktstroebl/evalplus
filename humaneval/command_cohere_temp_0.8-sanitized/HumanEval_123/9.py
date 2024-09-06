def get_odd_collatz(n):
    odd_collatz = [1]
    while len(odd_collatz) < n:
        if odd_collatz[-1] % 2 == 0:
            odd_collatz.append(odd_collatz[-1] // 2)
        else:
            odd_collatz.append(3 * odd_collatz[-1] + 1)
    return odd_collatz[:n]