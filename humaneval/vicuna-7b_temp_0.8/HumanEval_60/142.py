

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
    # Check if n is a positive integer
    if n >= 1:
        # Create an empty list
        numbers = []
        # Loop through the numbers from 1 to n
        for i in range(1, n+1):
            # Append each number to the list
            numbers.append(i)
        # Add the numbers in the list together
        return sum(numbers)
    else:
        return 0
