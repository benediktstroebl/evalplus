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
    # removing any non-numeric characters and converting to integer
    string = string.replace(' ', '')
    string = string.replace('(', '')
    string = string.replace(')', '')
    string = string.replace('-', '')
    string = string.replace('+', '')
    string = string.replace('^', '')
    string = string.replace(',', '')
    string = string.replace('/', '')
    string = string.replace('`', '')
    string = string.replace('~', '')
    string = string.replace('!', '')
    string = string.replace('"', '')
    string = string.replace('\\', '')
    string = string.replace('|', '')
    num = int(string)
    return is_prime(num)