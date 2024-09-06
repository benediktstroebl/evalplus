
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # your code here
    def is_prime(num):
        for n in range(2, int(num**(1/2))+1):
            if num % n == 0:
                return False
        return True
    if a < 100:
        count = 0
        for i in range(2,int(a**(1/2))+1):
            if a % i == 0:
                if is_prime(i):
                    count += 1
        if count == 3:
            return True
        return False
    else:
        return False

