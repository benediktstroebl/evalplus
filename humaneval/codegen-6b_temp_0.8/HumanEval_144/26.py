
def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """
    x,n = map(str,x.split('/'))
    n,d = int(n),int(x)
    for i in range(10**(n.__len__()-1),10**n.__len__()):
        xn,dn = str(i*d).split('/'),str(i).split('/')
        if xn[0] =='0' and xn[1]=='0':
            continue
        else:
            n2,d2 = int(n*i),int(x*i)
            if n2==d2:
                return True
    return False

