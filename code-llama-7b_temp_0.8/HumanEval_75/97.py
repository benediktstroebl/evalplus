
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # This function returns True if the given number is the multiplication of 3 prime numbers and false otherwise.
    # We write code inside the function.
    # We will use the if statement to decide if the number is or not the multiplication of 3 prime numbers.
    # We use the return keyword to return a value from the function.
    # True if the number is the multiplication of 3 prime numbers and False otherwise.
    
    # We need to check if the given number is the multiplication of 3 prime numbers.
    # We know that a < 100.
    # That means that the number should be less than 4 digits.
    # We will use the if statement to check if the number has 4 digits.
    if len(str(a)) != 4:
        # If the number does not have 4 digits, then the number is not the multiplication of 3 prime numbers.
        # We return False.
        return False
    
    # If the number has 4 digits, then we will check if the number is the multiplication of 3 prime numbers.
    # We will use the for loop to check if there are three prime numbers in the number.
    # We will start the first index from the first character and the last index from the last character.
    for i in range(0, 3):
        # We will check if the number is the multiplication of 3 prime numbers.
        # We will check if the number has three prime numbers.
        for j in range(i + 1, 4):
            # We will check if the number is the multiplication of 3 prime numbers.
            # We will check if the number is the multiplication of two prime numbers.
            for k in range(j + 1, 5):
                # We will check if the number is the multiplication of 3 prime numbers.
                # We will check if the number is the multiplication of one prime number.
                for l in range(k + 1, 6):
                    # We will check if the number is the multiplication of 3 prime numbers.
                    # If we found 3 prime numbers in the number, then we will return True.
                    if is_prime(a / (10 ** (l - 1))) and is_prime(a / (1
