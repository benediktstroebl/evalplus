
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    #  Your code here
    if len(str(n))==0:
        return 0
    else:
        result=[]
        for x in range(len(str(n))):
            if x%2 != 0:
                result.append(int(str(n)[x]))
        return result
