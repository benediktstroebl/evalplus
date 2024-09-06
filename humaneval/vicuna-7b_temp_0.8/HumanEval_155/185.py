
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    num = int(num)
    count = 0
    for i in str(num)[2:]:
        if i.is_even():
            count += 1
        else:
            count += 2
    return count, count + 1
