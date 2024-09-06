
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_counter = 0
    odd_counter = 0
    temp = num
    while temp > 0:
        if temp % 10 == 0:
            even_counter += 1
        else:
            odd_counter += 1
        temp = temp // 10
    return even_counter, odd_counter

