
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # Get the absolute value of the input number
    n = abs(num)

    # Get the absolute value of n as an int
    n_int = int(n)

    # Initialize the counter for even digits
    counter_even = 0
    # Initialize the counter for odd digits
    counter_odd = 0

    # Iterate over the digits of n
    for i in range(10):
        # Get the current digit of n
        digit = n_int % 10

        # Increment the counter for even digits
        if digit == 0:
            counter_even += 1
        # Increment the counter for odd digits
        else:
            counter_odd += 1

    return counter_even, counter_odd
