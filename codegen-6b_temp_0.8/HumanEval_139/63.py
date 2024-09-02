
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
    # Create a list of 1,2,3,4,5... elements
    # Set first element to 1 and second to 2
    # for n in range(2, n+1):
    #     # Multiply first element by n
    #     first_element *= n

    # Multiply first element by n-1
    first_element = 1
    for n in range(2, n + 1):
        first_element *= n

    # Multiply second element by n-2
    second_element = 1
    for n in range(2, n - 1):
        second_element *= n

    # Multiply third element by n-3
    third_element = 1
    for n in range(2, n - 2):
        third_element *= n

    return first_element * second_element * third_element
