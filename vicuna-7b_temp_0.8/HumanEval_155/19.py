
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    digits = str(num)
    odd_count = 0
    for i in range(len(digits) - 1):
        if digits[i] in '01':
            odd_count += 1
    return (len(digits) // 2 - odd_count, odd_count)
