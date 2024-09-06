def get_odd_collatz(n):
    odd_seq = [x for x in map(lambda x: x if x % 2 else x * 2, incubate(n)) if x % 2 == 1]
    return sorted(odd_seq)