
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    counter_odd = 0
    counter_even = 0
    if num >= 0:
        while num:
            if num % 10 % 2 == 1:
                counter_odd += 1
            else:
                counter_even += 1
            num //= 10
    else:
        num *= -1
        while num:
            if num % 10 % 2 == 1:
                counter_odd += 1
            else:
                counter_even += 1
            num //= 10
    return counter_odd, counter_even
