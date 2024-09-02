
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

    # These are examples of the tests that will fail.
    # After you write up your code, comment out the list.
    assert simplify("1/5", "5/1") == True
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/3", "1/3") == True
    assert simplify("1/4", "1/4") == True
    assert simplify("1/5", "1/5") == True
    assert simplify("1/6", "1/6") == True
    assert simplify("1/7", "1/7") == True
    assert simplify("1/8", "1/8") == True
    assert simplify("1/9", "1/9") == True
    assert simplify("1/10", "1/10") == True
    assert simplify("2/1", "4/1") == True
    assert simplify("3/1", "3/1") == True
    assert simplify("4/1", "2/1") == True
    assert simplify("5/1", "1/1") == True
    assert simplify("6/1", "1/2") == True
    assert simplify("7/1", "1/3") == True
    assert simplify("8/1", "1/4") == True
    assert simplify("9/1", "1/5") == True
    assert simplify("10/1", "1/6") == True
    assert simplify("11/1", "1/7") == True
    assert simplify("12/1", "1/8") == True
    assert simplify("13/1", "1/9") == True
    assert simplify("14/1", "1/10") == True
    assert simplify("15/1", "1/11") == True
    assert simplify("16/1", "1/12") == True
    assert simplify("17/1", "1/13") == True
    assert simplify("18/1", "1/14") == True
    assert simplify("19/1", "1/15") == True
    assert simplify("20/1", "1/16") == True
    assert simplify("21/1", "1/17
