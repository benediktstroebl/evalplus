
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    list1 = list(str(n))
    list2 = []
    for i in range(len(list1)):
        if i % 2 == 0:
            continue
        else:
            list2.append(list1[i])
    return int(''.join(list2))

