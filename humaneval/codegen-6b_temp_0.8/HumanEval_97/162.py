
def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    """
   
    def to_num(s):
        s = str(s)[::-1]
        l = [int(i) for i in s]
        return l[0]

    def to_unit(n):
        return n%10

    def helper(n):
        return n//10

    def recursive(a,b):
        if a == 0:
            return b
        if a < b:
            a,b = b,a
        r = helper(a)
        a = to_num(a)
        b = to_num(b)
        m = a*b
        r +=  m*to_unit(m)
        return recursive(r, b)

    return recursive(a,b)

"""