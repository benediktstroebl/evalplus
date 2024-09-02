
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # your code here
    if a < 100:
        numbers = []
        for i in range(2, 10):
            if a % i == 0:
                numbers.append(i)
        if len(numbers) == 3:
            return True
        else:
            return False
    else:
        return False
