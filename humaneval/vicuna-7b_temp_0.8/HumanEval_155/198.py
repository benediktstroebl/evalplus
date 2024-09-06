
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        return (0, 0)
    if num == 0:
        return (0, 1)
    # convert num to string
    num_str = str(num)
    # split the string into even and odd parts
    even_parts = num_str[:int(len(num_str)/2)]
    odd_parts = num_str[int(len(num_str)/2):]
    # count the number of digits in even and odd parts
    num_of_digits_even = sum([int(digit) for digit in even_parts])
    num_of_digits_odd = sum([int(digit) for digit in odd_parts])
    # return the number of even and odd digits
    return (num_of_digits_even, num_of_digits_odd)
