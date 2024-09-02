
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # Check if the number is negative
    if num < 0:
        return -1
    
    # Check if the number is zero
    if num == 0:
        return (0, 0)
    
    # Get the digits of the number
    digits = str(num)
    
    # Get the length of the number
    len_digits = len(digits)
    
    # Check if the number is odd
    if len_digits % 2 == 1:
        return (len_digits // 2, len_digits // 2 + 1)
    else:
        return (len_digits // 2, len_digits // 2)
