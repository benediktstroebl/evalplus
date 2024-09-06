
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    odd = 0
    even = 0
    num_string = str(num)
    for i in num_string:
        i = int(i)
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)

