
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    num = abs(int(num))
    if num == 0:
        return (0, 0)
    elif num % 2 == 0:
        return (int(num / 10), int(num % 10))
    return (int((num - 1) / 10), int((num - 1) % 10))
