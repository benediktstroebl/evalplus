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
    # Removing non-ascii characters, punctuation, and converting to ascii
    string = ''.join(c for c in string if ord(c) < 128)
    string = string.replace('.', '').replace('/', '').replace('-', '').replace('`', '').replace('^', '').replace('&', '').replace('=', '')
    string = string.strip('.,()-[]{}%:;')
    
    if len(string) == 0:
        return False
    return is_prime(len(string))