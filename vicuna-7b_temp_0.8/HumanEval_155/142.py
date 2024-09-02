
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # Adding 1 to the number and converting it to string will change the number of digits
    # but will not affect the digits themselves
    str_num = str(num + 1)
    # Even number of digits is a multiple of 4
    if len(str_num) % 4 == 0:
        num_digits = len(str_num) // 4
        return num_digits // 2, num_digits // 2 + 1
    else:
        # Odd number of digits is not a multiple of 4
        odd_digits = len(str_num) % 4
        num_digits = len(str_num) // 4
        return num_digits // 2, num_digits - odd_digits
