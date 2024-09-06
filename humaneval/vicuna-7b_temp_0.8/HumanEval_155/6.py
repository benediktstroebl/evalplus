
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num == 0:
        return (0, 0)
    digits = str(num)
    return_list = []
    for digit in digits:
        return_list.append(digit % 2)
    return_list.append(return_list[-1])
    return_list.insert(0, 1)
    return (len(return_list), len(return_list[1:]))
