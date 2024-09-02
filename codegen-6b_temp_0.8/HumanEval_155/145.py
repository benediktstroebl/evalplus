
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        return even_odd_count(-num)
    negative = 0
    if num < 0:
        num *= -1
        negative = 1
    ans = "odd"
    if num == 0:
        return (0, 0)
    else:
        i = 0
        while num >= 1:
            if i % 2 == 0:
                ans = "even"
            else:
                ans = "odd"
            num %= 10
            i += 1
    return (i - 1, negative)
