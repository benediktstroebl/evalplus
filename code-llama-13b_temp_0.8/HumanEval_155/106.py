
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    count = 0
    count1 = 0
    while num != 0:
        rem = num % 10
        if rem % 2 == 0:
            count += 1
        else:
            count1 += 1
        num //= 10
    return count, count1
