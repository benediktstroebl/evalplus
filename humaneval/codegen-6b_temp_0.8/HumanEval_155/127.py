
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if len(str(num)) == 1:
        return 0, 1
    elif len(str(num)) == 2:
        return 1, 1
    elif len(str(num)) % 2 == 0:
        return len(str(num)) / 2, len(str(num)) / 2
    elif len(str(num)) % 2 == 1:
        return len(str(num)) / 2 + 1, len(str(num)) / 2

