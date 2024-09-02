
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
    factorial_dict = {1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040}

    if n > 0:
        # The function will generate all the multiplications of the factorial
        # of n and put it in a list
        multiplication_list = []
        for i in range(1, n+1):
            multiplication_list.append(factorial_dict[i] * factorial_dict[n-i])
        # The function will return the sum of the elements of the list
        return sum(multiplication_list)
    else:
        # The function will return 1 if n <= 0
        return 1
