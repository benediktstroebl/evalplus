
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # Check if the number is negative
    if num < 0:
        return (0, 0)

    # Check if the number is an even number
    if num % 2 == 0:
        return (1, 1)

    # Check if the number is odd
    elif num % 2 != 0:
        return (1, 1)

    # Check if the number has 0 as the first digit
    if num == 0:
        return (0, 0)

    # If the number has digits other than 0
    return (int(num // 10), int(num % 10))
