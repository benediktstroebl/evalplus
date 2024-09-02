
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    digits = str(num).split('')
    count_of_even = 0
    count_of_odd = 0
    for i in range(len(digits)):
        if digits[i] == '0':
            count_of_even += 1
        else:
            count_of_odd += 1
    return (count_of_even, count_of_odd)
