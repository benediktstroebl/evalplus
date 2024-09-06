
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        return -1

    if str(num) == str(num):
        return 1, 1

    remainder = 0
    for num in str(num):
        remainder = remainder * 10 + (num % 2)

    return remainder, remainder // 2 + 1
