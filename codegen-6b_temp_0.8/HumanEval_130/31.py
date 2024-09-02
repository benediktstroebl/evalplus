
def tri(n):
    """Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8 
    You are given a non-negative integer number n, you have to a return a list of the 
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    tri(3) = [1, 3, 2, 8]
    """
    a, b, c = 1, 2, 1
    ret = []
    while len(ret) < n + 1:
        ret.append(a)
        a, b = b, c
        c = a + b
        if len(ret) == n + 1:
            return ret


cases = (
    (1, [1]),
    (2, [1, 2]),
    (3, [1, 3, 2]),
    (4, [1, 4, 5, 9]),
    (5, [1, 5, 8, 15, 21]),
    (6, [1, 6, 11, 20, 37, 58]),
    (7, [1, 7, 13, 28, 46, 85, 143]),
    (10, [1, 11, 22, 43, 87, 149, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946,
          17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269,
          2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986,
          99463598, 15496838, 25793459, 479001655, 7586269049, 12586269049]),
)

for i, (n, exp) in enumerate(cases):
    assert tri(n) == exp
