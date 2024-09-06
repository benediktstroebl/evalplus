
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num == 0:
        return 0, 0
    elif num < 0:
        return 0, -1
    elif num == 1:
        return 1, 0
    else:
        count_even = 0
        count_odd = 0
        i = 1
        while i <= min(num, len(str(num))):
            if num % i == 0:
                count_even += 1
                i += 1
            else:
                count_odd += 1
                i += 1
        return count_even, count_odd
