
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if not isinstance(num, int):
        raise TypeError("You must enter a valid integer")
    else:
        total_even = 0
        total_odd = 0
        num_str = str(num)
        for i in range(len(num_str)):
            if int(num_str[i]) % 2 == 0:
                total_even += 1
            else:
                total_odd += 1
    return total_even, total_odd
