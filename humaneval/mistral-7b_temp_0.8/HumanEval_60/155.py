

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
    num = 0
    while num < n:
        num = num + 1
    sum_num = 0
    while num >= 1:
        sum_num = sum_num + num
        num = num - 1
    return sum_num

