
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    odd_cnt = 0
    even_cnt = 0
    for i in range(len(num)):
        if num[i] % 2 == 0:
            even_cnt += 1
        else:
            odd_cnt += 1
    return (even_cnt, odd_cnt)
