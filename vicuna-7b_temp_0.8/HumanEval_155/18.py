
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        return -1
    else:
        digits = str(num)
        count_even = 0
        count_odd = 0
        for i in range(len(digits)):
            count_even += (digits[i] == '0')
            count_odd += (digits[i] == '1')
        return (count_even, count_odd)
