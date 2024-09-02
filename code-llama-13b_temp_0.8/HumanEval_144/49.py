
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
    def split_to_num_denom(x):
        x_list = x.split("/")
        num = int(x_list[0])
        denom = int(x_list[1])
        return (num, denom)
    
    num_1, denom_1 = split_to_num_denom(x)
    num_2, denom_2 = split_to_num_denom(n)
    num_3 = num_1*num_2
    denom_3 = denom_1*denom_2
    if num_3 % denom_3 == 0:
        return True
    else:
        return False
    
    
