
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # for i in range(1,100):
    #     # check if i is a prime number
    #     prime = True
    #     for j in range(2,i):
    #         if i % j == 0:
    #             prime = False
    #             break
    #     if prime:
    #         if a%i==0:
    #             count += 1
    #             if count == 3:
    #                 return True

    count = 0
    for i in range(1,100):
        # check if i is a prime number
        prime = True
        for j in range(2,i):
            if i % j == 0:
                prime = False
                break
        if prime:
            if a%i==0:
                count += 1
                if count == 3:
                    return True
    return False
