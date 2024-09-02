
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Define a variable to keep track of the current number of factors
    current_factors = 0
    # Iterate through all the numbers from 2 to the square root of (a-1)
    for i in range(2, int(np.sqrt(a-1))+1):
        # Keep track of the number of factors
        factors = 0
        for num in range(i+1, a+1):
            # If the number is prime, add 1 to the number of factors
            if num > 1 and (num % 2 == 0 or num % 3 == 0):
                factors += 1
            else:
                # If the number is prime, add 1 to the current number of factors
                factors += 1
                current_factors += 1
        # If the number of factors is less than 3, return True
        if factors < 3:
            return True
    # If the number of factors is 3 or more, return False
    return False
