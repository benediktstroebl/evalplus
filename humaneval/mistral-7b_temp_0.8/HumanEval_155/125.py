
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    counter = 0
    even_counter = 0
    for i in num:
        if i % 2 == 0:
            even_counter += 1
        else:
            counter += 1
    return (even_counter, counter)
