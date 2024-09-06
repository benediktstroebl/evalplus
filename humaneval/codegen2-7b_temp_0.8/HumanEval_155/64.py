
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    num_str = str(num)
    even_num = num_str.count('2')
    odd_num = num_str.count('3')
    return (even_num, odd_num
