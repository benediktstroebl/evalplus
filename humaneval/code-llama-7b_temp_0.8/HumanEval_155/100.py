
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # TThe number of even and odd digits.
    even, odd = 0, 0
    # Keep track of the number.
    number = abs(num)

    while number > 0:
        # Get the last digit of the number.
        digit = number % 10
        # Increment the counter of the even digit.
        if digit % 2 == 0:
            even += 1
        else:
            odd += 1
        # Remove the last digit from the number.
        number //= 10

    return (even, odd)
