
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    sum_even = 0
    sum_odd = 0
    for num in range(len(num)):
        if num%2 == 0:
            sum_even += 1
        else:
            sum_odd += 1
    return sum_even, sum_odd

