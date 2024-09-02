
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        return even_odd_count(-num)
    elif num == 0:
        return 0, 1
    else:
        cnt_odd, cnt_even = 1, 1
        while num >= 10:
            if num % 2 == 0:
                cnt_odd *= 10
                cnt_even *= 10
            else:
                cnt_odd *= 10
                cnt_even *= 10
            num = num // 10
        if num % 2 == 0:
            return cnt_even, cnt_odd
        else:
            return cnt_odd, cnt_even
