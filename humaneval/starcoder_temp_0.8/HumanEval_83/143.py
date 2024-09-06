
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    def is_one(s):
        return s[0] == '1' or s[-1] == '1'

    def convert(s):
        return int(s)

    return sum(1 for i in range(n)
               if is_one(str(i)) or is_one(str(convert(bin(i)[2:]))))
