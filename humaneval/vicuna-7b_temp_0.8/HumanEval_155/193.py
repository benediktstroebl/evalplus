
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        return (-1, -1)
    if not str(num).is_digit():
        return (-1, -1)
    else:
        num = int(str(num))
        count = 0
        for i in range(len(str(num))):
            if str(num)[i] in ['0', '1']:
                count += 1
        return (count % 2 == 0, count % 2)
