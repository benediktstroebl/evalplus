
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num == 0:
        return (0, 0)
    else:
        if num < 0:
            num = abs(num)
            sign = -1
        else:
            sign = 1
        nums = [x for x in str(num)]
        even = 0
        odd = 0
        for num in nums:
            if int(num) % 2 == 0:
                even += 1
            else:
                odd += 1
        return (sign * even, sign * odd)

