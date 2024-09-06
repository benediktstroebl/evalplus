
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

    nums = str(num)
    e = 0
    o = 0
    for i in nums:
        if int(i) % 2 == 0:
            e += 1
        else:
            o += 1
    return (e, o)



