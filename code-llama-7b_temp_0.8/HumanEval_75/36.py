
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a <= 100:
        prime_number_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        prime_number_multiply = []

        for i in range(len(prime_number_list)):
            if a % prime_number_list[i] == 0:
                prime_number_multiply.append(prime_number_list[i])
            if len(prime_number_multiply) == 3:
                return True
        return False

    return "Not a number less then 100"

