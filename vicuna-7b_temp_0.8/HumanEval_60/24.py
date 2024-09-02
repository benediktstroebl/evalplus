

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
    for i in range(2, n+1):
        sum_of_powers = (i - 1)**2
        add_to_sum = (i - 1)**2
        while sum_of_powers >= i:
            sum_of_powers -= i
            add_to_sum -= i
        sum_to_n(n) = sum_to_n(n) + add_to_sum + (i-1)
    return sum_to_n(n)

sum_to_n(int(input("Enter a number to sum from 1 to n: ")))