
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if not isinstance(num, int):
        raise TypeError("Only integers are allowed")
    num_str = str(abs(num))
    if num < 0:
        num_str = num_str[1:]
    return tuple(map(len, (filter(lambda x: int(x) % 2 == 0, num_str), filter(lambda x: int(x) % 2 != 0, num_str))))
