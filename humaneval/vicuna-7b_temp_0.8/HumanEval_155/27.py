
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    digits = str(num).split("")
    evens = 0
    odds = 0
    for i in range(len(digits)):
        if i % 2 == 0:
            evens += 1
            digits[i] = '0'
        else:
            odds += 1
    return (evens, odds)
