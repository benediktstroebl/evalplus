def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True
def prime_length(string):
    string = str(string)
    # checking if string of length 1 or 2 is prime
    if len(string) < 3:
        return True
    # transforming string into an integer to check if it's a prime length
    num = int(len(string))
    if is_prime(num):
        return True
    return False