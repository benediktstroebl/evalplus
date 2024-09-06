def get_odd_collatz(n):
    odd_seq = [y for y in collatz_sequence(n) if y % 2 == 1]
    return sorted(odd_seq)
def collatz_sequence(n):
    if n == 1:
        return [1]
    else:
        odd_seq = collatz_sequence(n // 2 if n % 2 == 0 else 3 * n + 1)
        even_seq = collatz_sequence(n // 2 if n % 2 == 0 else 3 * n + 1)
        return odd_seq + even_seq