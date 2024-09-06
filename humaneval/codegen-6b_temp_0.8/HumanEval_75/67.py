
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    prime_numbers = [2, 3, 5]
    for i in range(2, 100):
        if i % 2 == 0:
            continue
        for j in prime_numbers:
            if i % j == 0:
                break
            if j * j > i:
                prime_numbers.append(i)
                break
    for i in prime_numbers:
        if i > a:
            break
        if a % i == 0:
            return False
    return True

