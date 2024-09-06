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
    string = str(sum(map(ord, string)))
    # converting the sum to string to make it a valid hex string
    # adding 1 to ensure numbers like '111' are not considered prime
    return is_prime(int(string, 16) + 1)