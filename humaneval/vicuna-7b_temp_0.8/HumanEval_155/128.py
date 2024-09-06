
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        return (0, 0)
    result = []
    for i in range(len(str(num))):
        if str(num)[i] in '01':
            result.append(str(num)[i])
        else:
            result.append('')
    if len(result) % 2 == 0:
        return (len(result), len(result))
    else:
        return (len(result) - 1, len(result))

print(even_odd_count(123456789))  # (1, 2)
print(even_odd_count(0))        # (0, 0)
print(even_odd_count(-12345))  # (1, 1)