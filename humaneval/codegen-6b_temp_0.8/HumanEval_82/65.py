
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # If the length is not a prime number, the digits stored are not all unique.
    # But since we are only interested in primes, we can't have duplicate digits.
    # We can use the fact that a number is unique if there is only one copy of each
    # number. If the string is in alphabetical order, we will create a list of the
    # alphabetical order of the string. We can calculate the difference between the
    # first and the last instances of each letter. If this difference is not 1, then
    # the string is not a prime number.
    if len(string) == 0 or len(string) == 1:
        return True

    num = []
    for i in range(len(string)):
        num.append(string[i])

    for i in range(len(num)):
        if num.count(num[i]) > 1:
            return False

    return True

