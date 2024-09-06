def get_odd_collatz(n):
    odd_collatz = [3*i+1 for i in range(1, n+1, 2)]
    even_collatz = [i/2 for i in range(n, 1, 2)]
    odd_collatz.extend(even_collatz)
    return odd_collatz