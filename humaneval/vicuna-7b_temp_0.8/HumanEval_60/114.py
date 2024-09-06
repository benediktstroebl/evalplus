

def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    if n <= 1:
        return n
    else:
        result = 1
        for i in range(2, n+1):
            result += i
        return result

print(sum_to_n(50))  # should print 1355
print(sum_to_n(1000))  # should print 46500