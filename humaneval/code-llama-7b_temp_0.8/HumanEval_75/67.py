
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Your code here
    # FIRST SOLUTION - SLOW
    # prime_numbers = []
    # is_prime = False
    # for number in range(2, a+1):
    #     for divider in range(2, number):
    #         if number % divider == 0:
    #             is_prime = False
    #             break
    #     if is_prime:
    #         prime_numbers.append(number)
    # is_multiply_prime = False
    # for prime_number in prime_numbers:
    #     if prime_number * prime_number * prime_number == a:
    #         is_multiply_prime = True
    #         break
    # return is_multiply_prime

    # SECOND SOLUTION
    # prime_numbers = []
    # for number in range(2, a+1):
    #     for divider in range(2, number):
    #         if number % divider == 0:
    #             break
    #     else:
    #         prime_numbers.append(number)
    # is_multiply_prime = False
    # for i in range(len(prime_numbers)):
    #     for j in range(len(prime_numbers)):
    #         for k in range(len(prime_numbers)):
    #             if prime_numbers[i] * prime_numbers[j] * prime_numbers[k] == a:
    #                 is_multiply_prime = True
    #                 break
    #     if is_multiply_prime:
    #         break
    # return is_multiply_prime

    # THIRD SOLUTION - FAST
    for number_1 in range(2, int(a**(1/3))+1):
        for number_2 in range(2, int(a**(1/3))+1):
            if number_1 * number_2 >= a:
                break
            for number_3 in range(2, int(a**(1/3))+1):
                if number_1 * number_2 * number_3 == a:
                    return True
    
