def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0
    """
    factorials = [1]
    for i in range(2, n + 1):
        factorials.append(i * factorials[i - 1])
    return factorials[n]