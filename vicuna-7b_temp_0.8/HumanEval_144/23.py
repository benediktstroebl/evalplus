
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
    x, n = n.as_integer_ratio()
    return int(x) * int(n) == int(n)

test = [
("1/5", "5/1"),
("1/6", "2/1"),
("7/10", "10/2"),
("3/4", "4/3"),
("22/7", "7/3"),
("144/81", "81/37"),
("100/11", "9/11"),
("504/34", "34/11"),
("729/306", "306/109"),
("20/21", "21/20"),
("7/8", "8/7"),
("4/3", "3/4"),
("20/21", "21/20"),
("14/12", "12/14"),
("16/9", "9/16"),
("36/27", "27/36"),
("24/15", "15/24"),
("48/21", "21/48"),
("72/17", "17/72"),
("24/7", "7/24"),
("16/9", "9/16"),
("32/27", "27/32"),
("256/129", "129/256"),
("3/4", "4/3"),
("3/7", "7/3"),
("3/8", "8/3"),
("2/3", "3/2"),
("5/7", "7/5"),
("3/4", "4/3"),
("2/5", "5/2"),
("2/3", "3/2"),
("5/7", "7/5"),
("2/7", "7/2"),
("3/4", "4/3"),
("1/3", "3/1"),
("1/2", "2/1"),
("2/3", "3/
