def get_odd_collatz(n):
    odd_seq = [y for y in collatz_sequence(n) if y % 2 == 1]
    odd_seq.sort()
    return odd_seq
def collatz_sequence(n):
    if n == 1:
        return [1]
    else:
        odd_sequence = collatz_sequence(n//2 if n % 2 == 0 else 3*n+1)
        even_sequence = collatz_sequence(n//2 if n % 2 != 0 else 3*n+1)
        return odd_sequence + even_sequence