
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    lst=[]
    for i in str(n):
        if i.isdigit():
            lst.append(i)
    if lst.count('0') == len(lst):
        return 0
    else:
        return int(''.join([str(j) for j in lst if int(j) % 2 == 1]))

