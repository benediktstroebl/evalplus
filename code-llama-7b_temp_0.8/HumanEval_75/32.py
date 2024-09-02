
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Find Prime numbers
    prime_nums = []
    for i in range(2, a):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_nums.append(i)
    
    # Find the possible prime numbers of a
    possible_prime_nums = []
    for i in prime_nums:
        if a % i == 0:
            possible_prime_nums.append(i)
    if len(possible_prime_nums) > 3:
        return False
    if len(possible_prime_nums) < 3:
        return False

    return True
