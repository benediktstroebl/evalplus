
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # validate the input
    if not isinstance(num, int) or num < 0:
        raise TypeError("Only non-negative integers are allowed")

    return sum(int(char) % 2 == 0 for char in str(num)), sum(int(char) % 2 != 0 for char in str(num))

