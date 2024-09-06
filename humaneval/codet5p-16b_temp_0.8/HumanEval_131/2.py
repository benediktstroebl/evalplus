
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    digits_list = []
    i = 0
    while n!= 0:
        digits_list.append(n%10)
        n = n//10
    if len(digits_list) == 1:
        return digits_list[0]
    for i in digits_list:
        if i % 2!= 0:
            i = i
            return i*digits_list[1]
