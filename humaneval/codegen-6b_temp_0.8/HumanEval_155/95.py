
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num == 0:
        return(1, 1)
    elif num < 0:
        return(even_odd_count_helper(abs(num)))[::-1]
    n = num
    even_count = 0
    odd_count = 0
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        n //= 10
    return(odd_count, even_count)
