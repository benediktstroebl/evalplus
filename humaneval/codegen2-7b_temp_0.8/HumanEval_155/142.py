
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_digit_count = sum(x % 2 for x in str(num))
    odd_digit_count = len(str(num)) - even_digit_count
    return even_digit_count, odd_digit_count

