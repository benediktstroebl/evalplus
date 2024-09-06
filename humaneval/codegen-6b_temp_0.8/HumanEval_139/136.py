
def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    # Computes n!, all the way up to n = 1
    factorials = [1, 1]
    for i in range(2, n+1):
        factorials.append(factorials[i-1] * i)
    # Computes n-1!, all the way up to n = 1
    factorials_minus_one = [1, 1]
    for i in range(2, n):
        factorials_minus_one.append(factorials_minus_one[i-1] * (i+1))
    # Computes n-2!, all the way up to n = 1
    factorials_minus_two = [1, 1]
    for i in range(2, n-1):
        factorials_minus_two.append(factorials_minus_two[i-1] * i)
    # Computes n-3!, all the way up to n = 1
    factorials_minus_three = [1, 1]
    for i in range(2, n-2):
        factorials_minus_three.append(factorials_minus_three[i-1] * (i+1))
    # Computes 1!
    factorial_one = 1
    for i in range(1, n):
        factorial_one *= i
    return factorials[n] * factorials_minus_one[n-1] * factorials_minus_two[n-2] * factorials_minus_three[n-3] * factorial_one

