
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    digits=[]
    digit_list=list(str(n))
    digit_list.reverse()
    for i in range(len(digit_list)):
        if digit_list[i]%2!=0:
            digits.append(int(digit_list[i]))
    return 1 if len(digits)==0 else digits[0]*digits[-1]*(digits[-1]-1)
