
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Your code here
    n=str(n)
    if not n.isdigit() or len(n)==0 or n[0]=='0':
        return 0
    n=list(n)
    return reduce(lambda x, y: x*y if x*y!=0 and int(y)%2!=0 else x, n)
