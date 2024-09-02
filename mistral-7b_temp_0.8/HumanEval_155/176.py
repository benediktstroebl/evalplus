
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    sum_of_even = 0
    sum_of_odd = 0
    while(num > 0):
        x = num % 10
        if(x % 2 == 0):
            sum_of_even += 1
        else:
            sum_of_odd += 1
        num //= 10
    return sum_of_even, sum_of_odd

