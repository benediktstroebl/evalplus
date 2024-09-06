
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

    list_a = list(x)
    list_b = list(n)
    l_a = list_a[0]
    l_b = list_b[0]
    r_a = list_a[-1]
    r_b = list_b[-1]
    num1 = 0
    den1 = 0
    num2 = 0
    den2 = 0
    for i in range(1, len(list_a)):
        num1 = num1 * 10 + int(list_a[i])

    for j in range(1, len(list_b)):
        den1 = den1 * 10 + int(list_b[j])
    for i in range(1, len(list_a)):
        num2 = num2 * 10 + int(list_b[i])

    for j in range(1, len(list_b)):
        den2 = den2 * 10 + int(list_a[j])
    if (int(num1) * int(den2)) == (int
