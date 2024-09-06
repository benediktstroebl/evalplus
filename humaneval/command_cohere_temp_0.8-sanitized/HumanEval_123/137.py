def get_odd_collatz(n):
    odd_seq = [y for y in map(int, str(n)) if y % 2 == 1]
    collatz_seq = [y for y in odd_seq if y != 1]
    return sorted(collatz_seq)