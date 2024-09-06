
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Initialize variable as False
    is_prime = False
    
    # Check if the number is prime
    if a > 1:
        for num in range(2, int(a**0.5) + 1):
            if a % num == 0:
                is_prime = False
                break
        else:
            is_prime = True
    
    # Check if the number is the product of 3 prime numbers
    if is_prime == True:
        for num1 in range(2, int(a**0.5) + 1):
            for num2 in range(2, int(a**0.5) + 1):
                if a % (num1**3) == 0 and a % (num2**3) == 0:
                    for num3 in range(2, int(a**0.5) + 1):
                        if (num1**3) % num3 == 0 and (num2**3) % num3 == 0:
                            is_prime = False
                            break
                    else:
                        is_prime = True
                        break
    return is_prime
