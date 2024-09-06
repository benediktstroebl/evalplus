def make_a_pile(n):
    if n == 1:
        return [n]
    else:
        return [n] + odd_even(n + 1)
def odd_even(num):
    return [x for x in range(num, num + 2, 2 if num % 2 else 1)]