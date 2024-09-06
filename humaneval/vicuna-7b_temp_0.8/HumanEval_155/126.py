
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # The function does not check if the input is a positive integer, so it can take any value.
    # The function converts the input to a string and then converts it to an integer.
    # The function then checks the number of digits in the integer, and assigns the number of even and odd digits respectively.
    if str(num) == str(num):
        return int(num) % 2, int(num // 2)
    else:
        return int(num % 2), int(num // 2) + 1
