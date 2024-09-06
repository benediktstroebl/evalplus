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
    # removing any non char characters from the string and converting to lowercase to handle cases like 'Hello'
    string = ''.join(c for c in string if c.isalpha()).lower()
    return is_prime(len(string))