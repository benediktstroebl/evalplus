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
    # empty string or single character strings
    if not string or len(string) <= 1:
        return True
    # convert string to an integer
    int_string = int(string)
    if is_prime(int_string):
        return True
    return False