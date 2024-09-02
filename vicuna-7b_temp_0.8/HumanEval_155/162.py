
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    digits = str(num)
    count = 0
    for i in range(len(digits)):
        if digits[i] == '1':
            count += 1
        else:
            count -= 1
    return (count % 2, count // 2)