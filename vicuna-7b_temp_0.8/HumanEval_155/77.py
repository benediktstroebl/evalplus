
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # check if the number is positive
    if num > 0:
        # split the number into two parts
        num = str(num)
        num_parts = len(num)
        # check if the number is a power of 2
        if num % 2 == 0:
            even_parts = 2 * (num_parts // 2)
            odd_parts = num_parts % 2
        else:
            even_parts = num_parts
            odd_parts = 0
    else:
        # split the number into two parts
        num = str(num)
        num_parts = len(num)
        # check if the number is a power of 2
        if num % 2 == 0:
            even_parts = 2 * (num_parts // 2)
            odd_parts = 0
        else:
            even_parts = num_parts
            odd_parts = 1
    return (even_parts, odd_parts)
