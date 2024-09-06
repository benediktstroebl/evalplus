
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    user_input = str(num)
    return len(user_input) - len(user_input.rstrip('0')), len(user_input.rstrip('0'))
