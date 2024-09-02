
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    row_length = len(str(abs(num)))
    counted = [0, 0]
    for i in range(row_length):
        digit = abs(num) // 10 ** (row_length - i - 1) % 10
        if digit % 2 == 0:
            counted[0] += 1
        else:
            counted[1] += 1
    return counted
