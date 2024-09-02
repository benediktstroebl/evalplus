
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
    # PSEUDO
    # step 1: create function
    # step 2: split str into numerator and denominator for x
    # step 3: split str into numerator and denominator for n
    # step 4: multiply num_1 with den_2
    # step 5: multiply num_2 with den_1
    # step 6: if result is evenly divisible then return True, if not, return False

    def get_numerator_and_denominator(string):
        num_and_den = string.split("/")
        return int(num_and_den[0]), int(num_and_den[1])

    def simplify(x, n):
        num_1, den_1 = get_numerator_and_denominator(x)
        num_2, den_2 = get_numerator_and_denominator(n)
        num_3 = num_1 * den_2
        den_3 = den_1 * num_2
        return (num_3 % den_3) == 0
    return simplify

