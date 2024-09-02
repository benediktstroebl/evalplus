
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    def is_prime(n, min_value):
        if n < min_value:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    a = int(input("Enter a positive integer less than 100: "))
    for i in range(a, 101):
        if is_prime(i, a):
            for j in range(i + 1, 101):
                if is_prime(j, a):
                    if (i * j) % a == 0:
                        return True
    return False
