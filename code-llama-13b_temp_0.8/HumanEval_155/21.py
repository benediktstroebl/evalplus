
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    num = abs(num)
    digit_lst = list(map(int, str(num)))
    even_cnt = len(list(filter(lambda x: x % 2 == 0, digit_lst)))
    odd_cnt = len(list(filter(lambda x: x % 2 != 0, digit_lst)))
    return (even_cnt, odd_cnt)

