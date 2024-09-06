

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
    # smallest number
    smallest = 1
    # largest number
    largest = n
    # total of sums
    total = 0
    # loop from smallest to largest, add numbers to total
    for num in range(smallest, largest+1):
        total += num
    # return the total
    return total
