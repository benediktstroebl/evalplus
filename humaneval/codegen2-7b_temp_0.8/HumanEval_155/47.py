
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num == 0:
        return 0, 0
    else:
        return len([d for d in str(num) if d == '2']), len([d for d in str(num) if d == '1'
