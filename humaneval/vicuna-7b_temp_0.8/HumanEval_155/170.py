
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    num = int(num)
    if num < 0:
        return (-1, -1)
    if num == 0:
        return (0, 0)
    if num < 10:
        return (num, 0)

    digit_list = str(num).split('')
    even_count = 0
    odd_count = 0
    for i in range(len(digit_list)):
        if digit_list[i] in '01':
            odd_count += 1
        else:
            even_count += 1

    return (even_count, odd_count)