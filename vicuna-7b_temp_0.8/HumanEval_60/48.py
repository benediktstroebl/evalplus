

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
    if n == 0:
        return 0
    else:
        for i in range(1, n+1):
            sum = sum_to_n(i) + sum_to_n(n-i)
            if i % 2 == 0:
                sum *= i
            else:
                sum *= n-i
            if i > 1:
                sum *= (i-1)
            if n > 1:
                sum *= (n-1)
            if n > 1:
                sum *= (n-2)
        return sum
