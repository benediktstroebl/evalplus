

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

    n1 = 1
    n2 = 1
    sum = 0
    while (n1 <= n):
        while(n1 <= n):
            sum = n1 + n2
            n2 = n1
            n1 = sum
            print(n1)
        n1 = 1
        n2 = 1
    return sum

