
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    s = str(n)
    if s.count("1") == 0 and s.count("2") == 0 and s.count("3") == 0 and s.count("4") == 0 and s.count("5") == 0 and s.count("6") == 0 and s.count("7") == 0 and s.count("8") == 0 and s.count("9") == 0:
        return 0
    else:
        return int(s[-1]) * int(s[-2]) * int(s[-3]) * int(s[-4]) * int(s[-5]) * int(s[-6]) * int(s[-7]) * int(s[-8]) * int(s[-9])
