
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    digits = list(map(int, str(abs(num))))
    odd_count = 0
    even_count = 0
    for d in digits:
        if d % 2:
            odd_count += 1
        else:
            even_count += 1
    return (even_count, odd_count)
