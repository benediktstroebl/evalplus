def get_odd_collatz(n):
    odd_seq = [y for y in collatz_seq(n) if y % 2 == 1]
    return sorted(odd_seq)
def collatz_seq(n):
    if n == 1:
        return [1]
    else:
        yield from collatz_seq(n // 2 if n % 2 == 0 else 3 * n + 1)
        yield n