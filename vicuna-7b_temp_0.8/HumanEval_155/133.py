
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # if num < 0, return None
    if num < 0:
        return None
    
    # convert num to str
    num_str = str(num)
    
    # count the number of digits in the string
    num_digits = len(num_str)
    
    # create a list of even and odd digits
    even_odd_digits = []
    for i in range(num_digits):
        even_odd_digits.append(num_str[i] % 2 == 0)
    
    # return the number of even and odd digits in the string
    return (num_digits // 2, len(even_odd_digits))
