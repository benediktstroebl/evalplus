
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    n = int(x)
    m = int(y)
    if n > m:
        n, m = m, n

    i = n // 2
    while i * 2 < m:
        i = i + 1
    if i * 2 == m:
        return i
    else:
        return -1

