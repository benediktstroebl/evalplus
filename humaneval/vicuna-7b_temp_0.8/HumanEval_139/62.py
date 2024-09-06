
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
    # Print the number of ways to roll a die
    print(f"There are {n} ways to roll a die.")
    
    # Print the list of all factorials
    print("1! = ", n! + 1)
    
    # Calculate the sum of the factorials
    total_sum = sum(1 for i in range(1, n+1))
    
    # Multiply the list of factorials
    for i in range(1, n+1):
        total_sum *= i
    
    # Return the special factorial
    return total_sum
