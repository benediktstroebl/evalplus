
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    digits = str(num)
    even = 0
    odd = 0
    for i in range(len(digits)-1):
        if digits[i] == '0':
            even += 1
        else:
            odd += 1
    return (even, odd)
