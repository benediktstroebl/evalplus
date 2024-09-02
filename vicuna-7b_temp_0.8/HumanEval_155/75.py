
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    num = int(num)
    if num == 0:
        return 1, 0
    result = 0
    for i in range(len(str(num))):
        if str(num)[i] == '0':
            result += 1
    if num % 2 == 0:
        return (result, 1)
    else:
        return (result + 1, 1)
