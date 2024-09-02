
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # base case
    if num == 0:
        return (0, 0)
    else:
        # get absolute
        abs_num = abs(num)
        # count 1's and 2's
        count = 0
        while abs_num > 0:
            if abs_num % 10 == 1:
                count += 1
            elif abs_num % 10 == 2:
                count += 1
            abs_num /= 10
        if num < 0:
            return (count, 1 - count)
        else:
            return (count, count)

