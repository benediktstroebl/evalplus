
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        return (1, 1)
    count = 0
    for i in str(num):
        if i == '0':
            count += 1
    if count % 2 == 1:
        return (count + 1, count)
    else:
        return (count, count
