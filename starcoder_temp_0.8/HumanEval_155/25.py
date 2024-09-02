
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num == 0:
        return 0, 0
    num_str = str(abs(num))
    even_cnt = len([i for i in num_str if int(i) % 2 == 0])
    odd_cnt = len([i for i in num_str if int(i) % 2!= 0])
    return even_cnt, odd_cnt

