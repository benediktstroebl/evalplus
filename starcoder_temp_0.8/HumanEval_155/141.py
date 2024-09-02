
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        num = abs(num)
    x = str(num)
    return (x.count('0')+x.count('2')+x.count('4')+x.count('6')+x.count('8'), x.count('1')+x.count('3')+x.count('5')+x.count('7')+x.count('9'))
