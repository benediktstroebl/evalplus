
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

    i = 0
    odd_count = 0
    even_count = 0

    while i <= len(num):
        if int(num[i]) % 2 != 0:
            odd_count += 1
        else:
            even_count += 1
        i += 1
    return (odd_count, even_count)
