
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
    list1 = x.split("/")
    list2 = n.split("/")
    list1[0] = int(list1[0])
    list1[1] = int(list1[1])
    list2[0] = int(list2[0])
    list2[1] = int(list2[1])
    a = list1[0] * list2[1]
    b = list1[1] * list2[0]
    if a%b==0:
        return True
    else:
        return False






