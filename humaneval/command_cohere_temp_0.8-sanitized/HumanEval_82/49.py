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
    string = str(sum(map(lambda x: ord(x), string)))
    # converting sum to int as sum of characters is always an integer
    # and converting using int() to keep it compatible with older versions
    return is_prime(int(string))