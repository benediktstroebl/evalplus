
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if not num:
        return (0,0)
    even_count = 0
    odd_count = 0
    if num >= 0:
        num_str = str(num)
        even_count = len(list(filter(lambda x: int(x)%2==0, num_str)))
        odd_count = len(list(filter(lambda x: int(x)%2!=0, num_str)))
    return (even_count, odd_count)

