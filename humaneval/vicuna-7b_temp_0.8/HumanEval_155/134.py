
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # str to int conversion
    n = int(num)
    # check for negative number
    if n < 0:
        return even_odd_count(-n)

    # find the number of digits in the number
    digits = sum(1 for i in range(n))

    # check if the number is even or odd
    if n % 2 == 0:
        even_count = digits // 2
        odd_count = digits % 2
    else:
        even_count = 0
        odd_count = digits // 2

    return (even_count, odd_count)
