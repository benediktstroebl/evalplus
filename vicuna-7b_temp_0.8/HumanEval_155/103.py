
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    digits = str(num)
    length = len(digits)
    even_count = length // 2
    odd_count = length % 2
    return int(even_count), int(odd_count)
