
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        return -1
    if not (num > 0):
        return -1
    digits = str(num)
    count_even = 0
    count_odd = 0
    for i in range(len(digits)):
        if digits[i] == '0':
            count_even += 1
            if digits[i - 1] == '0':
                count_odd += 1
        else:
            count_even = 0
            count_odd = 0
    return (count_even, count_odd)
