def is_multiply_prime(a):
    # Write a function that returns true if the given number is the multiplication of 3 prime numbers
    # and false otherwise
    if a < 100 and a > 0:
        num = a
        for i in range(2, int(num ** (0.5)) + 1):
            if num % i == 0:
                return False
        return num != 1 and is_multiply_prime(num)
    return False