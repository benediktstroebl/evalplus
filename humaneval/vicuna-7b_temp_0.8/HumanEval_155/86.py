
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    digits = str(num)
    odd_count = 0
    for i in range(len(digits)):
        if digits[i] in '01':
            odd_count += 1
    even_count = len(digits) - odd_count
    return odd_count, even_count
