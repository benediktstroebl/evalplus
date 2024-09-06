
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    string = str(n)
    new_list = []
    for i in range(0, len(string)):
        if int(string[i]) % 2 == 0:
            continue
        else:
            new_list.append(int(string[i]))
    if new_list == []:
        return 0
    else:
        return new_list[0] * new_list[1] * new_list[2]
