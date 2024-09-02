
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    count = 0
    a = abs(num)
    if num < 0:
        num = abs(num)
    while a >= 10:
        if int(a % 10) % 2 == 0:
            count += 1
        elif int(a % 10) % 2 != 0:
            count += 1
        a = a / 10
    return (count, a)
    
'''
