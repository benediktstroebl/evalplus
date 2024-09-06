def get_odd_collatz(n):
    odd_collatz = [num for num in map(lambda x: x*2+1 if x%2 else x/2, range(n, 0, -1))]
    return odd_collatz