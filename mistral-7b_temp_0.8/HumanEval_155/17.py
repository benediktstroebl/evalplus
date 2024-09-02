
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    ctr = 0
    ctr_odd = 0
    for i in str(num):
        if i % 2 == 0:
            ctr += 1
        else:
            ctr_odd += 1
    return ctr, ctr_odd

