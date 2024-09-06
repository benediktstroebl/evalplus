
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    result = [False, False, False]
    for i in range(2, min(a / 3, 10)):
        if i * i <= a:
            for j in range(2, a / (i * i)):
                if j * j * j <= a:
                    if a % (i * i * j) == 0:
                        result[0] = True
                        break
            if result[0] == False:
                break
    # if result[0] == True:
    #     print(i)
    if (a / 2) % i == 0:
        result[1] = True

    if a % i == 0:
        result[2] = True
    result = all(result)
    return result
