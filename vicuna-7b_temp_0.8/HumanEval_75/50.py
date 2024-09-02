
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    def __prime_check(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    a = int(input("Enter a number less than 100: "))

    if a < 2 or __prime_check(a) == False:
        return False
    p1 = 2
    for i in range(a-1, int(a**0.5)+1, 2):
        p2 = 2
        for j in range(i+1, int(a**0.5)+1, 2):
            if (i*j) % a == 0:
                p1 = i
                p2 = j
        if p1 == p2:
            return False
    return True