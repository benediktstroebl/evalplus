
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        num = -num
    num_str = str(num)
    even_num_count = 0
    odd_num_count = 0
    for i in num_str:
        if int(i) % 2 == 0:
            even_num_count += 1
        else:
            odd_num_count += 1
    return (even_num_count, odd_num_count)
