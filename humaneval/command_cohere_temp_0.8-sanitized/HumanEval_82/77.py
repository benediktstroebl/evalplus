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
    string = str(sum(map(ord, string)))
    # converting the sum to string to make sure the
    # sum of same characters will be treated as same string
    # e.g. str(97) == '97' and str(97) == '121'
    return is_prime(len(string))