def get_odd_collatz(n):
    if n <= 1:
        return [n]
    sequence = [n]
    for _ in range(1, int(n**0.5) + 1):
        sequence.append(int(n% + n - 2))
    return list(sequence)[::-1]