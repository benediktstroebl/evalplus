
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        return (-1, -1)
    digits = str(num)
    count_even = 0
    count_odd = 0
    for i in range(len(digits)):
        if digits[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            count_even += int(digits[i])
        else:
            count_odd += int(digits[i])
    return (count_even, count_odd)
