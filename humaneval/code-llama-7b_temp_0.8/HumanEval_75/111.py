
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    #first try to find the prime numbers. We need to find the factors to divide a and look for the numbers that
    #have a divisor
    prime_numbers = []
    for i in range(2, a+1):
        if a % i == 0:
            prime_numbers.append(i)
    
    #if the size of the prime numbers is different to 3, the number a isn't the multiplication of 3 prime numbers
    if len(prime_numbers) != 3:
        return False
    
    #if the prime numbers are different than 2,3,5 it isn't the multiplication of 3 prime numbers
    if prime_numbers[0] == 2 and prime_numbers[1] == 3 and prime_numbers[2] == 5:
        return True
    return False
