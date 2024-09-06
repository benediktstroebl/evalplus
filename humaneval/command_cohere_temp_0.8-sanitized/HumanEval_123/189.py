def get_odd_collatz(n):
    odd_seq = [x for x in map(int, str(n)) if x % 2 != 0]
    collatz_seq = [x for x in map(int, str(n)) if x != 1]
    return sorted(collatz_seq[:len(odd_seq)])