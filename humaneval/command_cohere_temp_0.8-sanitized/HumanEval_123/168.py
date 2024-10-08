def get_odd_collatz(n):
    odd_seq = [3*i+1 for i in range(1, n+1, 2)]
    even_seq = [i//2 for i in range(n, 1, 2)]
    odd_seq.extend(even_seq)
    return odd_seq