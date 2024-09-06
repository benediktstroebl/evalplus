
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

    if num < 0:
        even = -1
    else:
        even = 0

    if num % 2 == 0:
        odd = 1
    else:
        odd = 1

    for i in str(abs(num)):
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1

    return (even, odd)

