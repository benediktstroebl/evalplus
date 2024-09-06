def get_odd_collatz(n):
    odd_collatz = [3*i+1 for i in range(1, n+1, 2)]
    even_collatz = [i for i in range(n, 1, -2)]
    return odd_collatz + [i for i in even_collatz if i % 2 == 1]