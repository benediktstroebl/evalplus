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
    # removing any non char bits and converting to utf-8 simplifies the problem
    string = remove_non_char(string)
    return is_prime(len(string))
def remove_non_char(string):
    return ''.join(char for char in string if char.isalpha())