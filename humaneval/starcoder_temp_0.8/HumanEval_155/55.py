
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    count = 0
    while num > 0:
        if num % 2 == 0:
            count += 1
        num = num // 10
    return (count, len(str(num)))
