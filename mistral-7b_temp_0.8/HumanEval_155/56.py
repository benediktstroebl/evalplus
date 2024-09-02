
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    count = 0
    even_count = 0
    for i in range(len(str(num))):
        if num % 2 == 0:
            even_count += 1
        else:
            count += 1
    return even_count, count

