
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = odd_count = 0
    for n in str(num):
        if n == "0":
            pass
        elif int(n) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)

