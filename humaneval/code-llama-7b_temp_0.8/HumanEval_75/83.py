
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # multiply = 1
    # prime = 0
    # for i in range(3, 100, 2):
    #     for j in range(2, i):
    #         if i % j == 0:
    #             break
    #     else:
    #         prime += 1
    #         if prime == 3:
    #             multiply = i
    #             break
    # return a == multiply
    list_of_prime_nums = []
    is_prime_number = True
    if a <= 100:
        for i in range(2, a):
            is_prime_number = True
            for j in range(2, i):
                if i % j == 0:
                    is_prime_number = False
                    break
            if is_prime_number:
                list_of_prime_nums.append(i)
        return a == list_of_prime_nums[0] * list_of_prime_nums[1] * list_of_prime_nums[2]
    else:
        return False
    
