def get_odd_collatz(n):
    odd_seq = [3*i+1 for i in range(1, n//2 + 1)] if n % 2 else [1]
    even_seq = [x//2 for x in range(n, 1, -1)]
    return odd_seq + [x for x in even_seq if x % 2 == 1]