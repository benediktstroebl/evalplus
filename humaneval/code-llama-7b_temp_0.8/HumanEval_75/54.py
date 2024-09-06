
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 100:
        lst = list(range(2,a+1))
        prime_nums = []
        for x in lst:
            if is_prime(x):
                prime_nums.append(x)
            if len(prime_nums) == 3:
                if a == prime_nums[0] * prime_nums[1] * prime_nums[2]:
                    return True
                else:
                    return False
        return False
    
