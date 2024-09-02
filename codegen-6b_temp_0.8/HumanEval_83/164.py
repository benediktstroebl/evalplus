
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    f = [1]
    if n == 1:
        return f[0]
    f.append(0)
    while n > 9:
        f1 = [0]
        f2 = [0]
        i = 1
        while f[i] > 0:
            f1 = [1] + f1 + [0]
            f2 = [1] + f2 + [0]
            i += 1
        f = f1 + f2
        n = n // 10
    f1 = [1] + f1 + [0]
    f2 = [1] + f2 + [0]
    f = f1 + f2
    return sum(f)

assert(starts_one_ends(1) == 0)
assert(starts_one_ends(2) == 4)
assert(starts_one_ends(3) == 16)
assert(starts_one_ends(4) == 256)
assert(starts_one_ends(5) == 1024)
assert(starts_one_ends(6) == 4608)
assert(starts_one_ends(8) == 9216)
assert(starts_one_ends(10) == 2160)
assert(starts_one_ends(12) == 6152)
assert(starts_one_ends(18) == 109590)
assert(starts_one_ends(21) == 1815808)
