

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

    
    assert n >= 1, "The number should be greater than 1"
    
    sum_number = 0
    
    for i in range(1,n+1):
        sum_number += i
        
    return sum_number


