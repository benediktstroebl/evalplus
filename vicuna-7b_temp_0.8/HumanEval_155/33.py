
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num == 0:
        return (0, 0)
    else:
        result = []
        for i in range(len(str(num))):
            if str(num)[i] in ['0', '1']:
                result.append(1)
            else:
                result.append(0)
        if len(result) % 2 == 0:
            return (int(result[::2][::-1]), int(result[1::2]))
        else:
            return (int(result[::2]), int(result[1::2][::-1]))
