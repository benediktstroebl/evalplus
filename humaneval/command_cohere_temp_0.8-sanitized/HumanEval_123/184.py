def get_odd_collatz(n):
    odd_collatz = [1] if n == 1 else [1, n]
    while len(odd_collatz) < len(str(n)) :
        if odd_collatz[-1] % 2 == 0:
            odd_collatz.extend(x // 2 for x in odd_collatz)
        else:
            odd_collatz.extend(x * 3 + 1 for x in odd_collatz)
    return odd_collatz