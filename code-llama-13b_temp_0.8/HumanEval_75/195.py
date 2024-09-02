
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    prime_list = []
    for i in range(2,100):
        flag = True
        for j in prime_list:
            if i % j == 0:
                flag = False
                break
        if flag == True:
            prime_list.append(i)

    # prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for prime in prime_list:
        if a % prime == 0:
            a = a / prime

    if a == 1:
        return True
    else:
        return False

