
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
    brazilian_factorial_list = [1]
    for i in range(1, n):
        brazilian_factorial_list.append(i * brazilian_factorial_list[i - 1])
    return sum(brazilian_factorial_list)

