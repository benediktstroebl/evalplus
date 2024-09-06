def get_odd_collatz(n):
    odd_collatz = [y for y in collatz(n) if y % 2 != 0]
    return sorted(odd_collatz)
def collatz(n):
    if n == 1:
        return [1]
    if n % 2 == 0:
        return collatz(n // 2) + [n // 2]
    else:
        return collatz(3 * n + 1) + [3 * n + 1]