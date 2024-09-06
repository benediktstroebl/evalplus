def get_odd_collatz(n):
    odd_collatz = [y for y in iter_collatz(n) if y % 2 == 1]
    return sorted(odd_collatz)
def iter_collatz(n):
    yield n
    if n == 1:
        return
    if n % 2 == 0:
        yield from iter_collatz(n // 2)
    else:
        yield from iter_collatz(3 * n + 1)