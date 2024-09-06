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
    # converting string to int to handle cases like "12a"
    if len(string) == 0 or len(string) == 1:
        return False
    elif is_prime(int(len(string))):
        return True
    else:
        return False