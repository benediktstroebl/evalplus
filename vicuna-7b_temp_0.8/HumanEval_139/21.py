
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
    # Create an empty list
    factors = []

    # Get the digits of the number
    digits = str(n)
    # Convert the digits to an integer
    n = int(digits, 10)

    # Calculate the factorial of n
    n_factors = n * (n - 1) * (n - 2) * ... * 1

    # Create a loop to find the brazilian factorial
    while n_factors > 0:
        # Get the last digit of n_factors
        last_digit = n_factors % 10

        # Add 1 to the factors list
        factors.append(1)
        # Multiply the factors list by n
        factors = factors * n
        # Multiply the factors list by the last digit of n_factors
        factors = factors * last_digit
        # Subtract n_factors from n_factors
        n_factors = n_factors // 10

    # Return the factors list
    return factors
