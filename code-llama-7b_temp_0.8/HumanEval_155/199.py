
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even = 0
    odd = 0

    # your code here
    str = str(num)
    if len(str) == 1:
        if int(str) % 2 == 0:
            even += 1
        else:
            odd += 1
        return even, odd
    else:
        for i in str:
            if int(i) % 2 == 0:
                even += 1
            else:
                odd += 1
        return even, odd

