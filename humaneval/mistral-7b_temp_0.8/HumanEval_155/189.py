
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

    evencount = 0
    oddcount = 0

    if num < 0:
        num = -1 * num

    while num > 0:
        num = num//10
        evencount += 1
        oddcount += 1

    return (oddcount, evencount)
