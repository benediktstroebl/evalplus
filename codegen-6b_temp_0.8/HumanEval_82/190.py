
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if len(string) == 1:
        return False
    if string == string[::-1]:
        return True
    for i in range(len(string)):
        if isPrime(i):
            first_half = string[:i]
            last_half = string[i+1:]
            last_part = string[-1*(i+1):-1]
            second_part = string[-1*i:-1]
            if first_half == first_half[::-1] and last_half == last_half[::-1] and second_part == second_part[::-1]:
                return True

    return False

