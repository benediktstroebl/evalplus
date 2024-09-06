def get_odd_collatz(n):
    odd_collatz = []
    sequence = [n]
    while len(sequence) > 1:
        if sequence[-1] % 2 == 1:
            odd_collatz.append(sequence[-1])
        if sequence[-1] > 1:
            sequence.extend([sequence[-1] // 2, sequence[-1] * 3 + 1])
        sequence.pop()
    return odd_collatz