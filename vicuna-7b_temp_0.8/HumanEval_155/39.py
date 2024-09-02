
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # convert the number to a string and convert the string to a number
    num_str = str(num)
    num_num = int(num_str)

    # if the number is negative, return (0, 0)
    if num < 0:
        return (0, 0)

    # check if the number is even or odd
    if num_num % 2 == 0:
        return (1, 0)
    else:
        return (0, 1)
