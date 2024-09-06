def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True
def prime_length(string):
    string = str(string)
    # converting string to int to calculate length
    length = int(len(string))
    if length <= 1:
        return False
    if is_prime(length):
        return True
    else:
        return False