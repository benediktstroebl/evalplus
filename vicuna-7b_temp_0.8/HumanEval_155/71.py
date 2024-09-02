
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        return -1
    digits = str(num)
    num_digits = len(digits)
    even_count = 0
    odd_count = 0
    for i in range(1, num_digits):
        if digits[i] in '0468':
            even_count += 1
            odd_count = 0
        elif digits[i] in '2379':
            odd_count += 1
            even_count = 0
        else:
            break
    return (even_count, odd_count)
