def get_odd_collatz(n):
    odd_collatz = [x for x in collatz(n) if x % 2 != 0]
    return sorted(odd_collatz)
def collatz(n):
    if n == 1:
        return [1]
    elif n % 2 == 0:
        return collatz(n // 2) + [n // 2]
    else:
        return collatz(3 * n + 1) + [3 * n + 1]