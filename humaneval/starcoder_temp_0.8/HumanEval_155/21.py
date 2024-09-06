
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

    number = abs(num)
    count = [0, 0]
    while number > 0:
        number, digit = divmod(number, 10)
        if digit % 2:
            count[0] += 1
        else:
            count[1] += 1

    return tuple(count)
