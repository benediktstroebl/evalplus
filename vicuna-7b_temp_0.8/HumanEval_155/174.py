
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # Use the binomial theorem to calculate the sum of the digits
    sum_of_digits = 0
    while num > 0:
        num, remainder = divmod(num, 10)
        sum_of_digits += remainder
    return num, sum_of_digits - sum(map(int, str(num))) % 2
