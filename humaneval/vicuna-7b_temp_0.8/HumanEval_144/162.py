
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
    numerator, denominator = map(int, (x[0], n[0]))
    numerator_digits = str(numerator)
    denominator_digits = str(denominator)
    if denominator_digits == "0":
        return False
    while denominator_digits != "0":
        if denominator_digits[0] == denominator[0]:
            denominator_digits = denominator_digits[1:]
        elif denominator_digits[0] == "5":
            if denominator_digits == "50" or denominator_digits == "500" or denominator_digits == "5000":
                if numerator_digits == "1" or numerator_digits == "2" or numerator_digits == "3" or numerator_digits == "4" or numerator_digits == "6":
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    return False

x = ["1/5", "1/6", "7/10"]
for i in range(len(x)):
    y = simplify(x[i], x[i+1])
    print(y)