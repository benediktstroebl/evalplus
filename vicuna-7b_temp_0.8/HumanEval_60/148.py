

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
    if n > 0:
        # check if n is odd, if so, sum up the odd numbers and divide by 2
        if n % 2 == 1:
            result = sum_to_n(n // 2)
            if n % 2 == 1:
                result += 1
            return result
        # check if n is even, if so, sum up the even numbers
        else:
            result = sum_to_n(n // 2)
            return result
    else:
        return 0
