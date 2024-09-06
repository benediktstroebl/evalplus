def get_odd_collatz(n):
    odd_collatz = [3*i+1 for i in range(1, n+1, 2)] + [i for i in range(3, n+1, 2) if i%2]
    return odd_collatz