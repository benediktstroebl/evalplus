
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        return -1

    if not str(num).isdigit():
        return -1

    num_str = str(num)
    result = []
    for i in range(len(num_str)):
        if num_str[i] in '0123456789':
            result.append(num_str[i])
        else:
            break
    else:
        result.append(num_str[-1])
    return result
