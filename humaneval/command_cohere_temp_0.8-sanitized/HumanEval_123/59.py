def get_odd_collatz(n):
    odd_seq = [x for x in map(int, str(n)) if x & 1 == 1]
    collatz_seq = [x for x in odd_seq if x != 1]
    return sorted(collatz_seq)