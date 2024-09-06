
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    is_prime = [2]
    # for i in range(3, a, 2):
    #     for j in is_prime:
    #         if i % j == 0:
    #             break
    #     else:
    #         is_prime.append(i)

    # return True if len(is_prime) == a
    isPrimeList = [True] * (a // 2)
    for i in range(3, int(a ** .5) + 1, 2):
        if isPrimeList[i // 2]:
            j = 2 * i
            while j < a:
                isPrimeList[j // 2] = False
                j += i
    return True if sum(isPrimeList) == a else False

