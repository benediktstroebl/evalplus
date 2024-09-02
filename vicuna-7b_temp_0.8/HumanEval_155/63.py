
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    num = str(num)
    if num[0] == '0':
        num = num[1:]
    return len(num) % 2, len(num) // 2
