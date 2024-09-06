def get_odd_collatz(n):
    odd_seq = [x for x in map(int, str(n)) if x % 2 == 1]
    collatz_seq = [x for x in map(int, str(n)) if x != 1]
    return sorted(odd_seq + [x for x in collatz_seq if x % 2 == 1])