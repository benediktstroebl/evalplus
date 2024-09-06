
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    def is_prime(num):
        # if num is less than 2, return false
        if num < 2:
            return False
        # loop through all numbers up to num
        for i in range(2, num):
            # if i is a factor of num, return false
            if num % i == 0:
                return False
        # otherwise return true
        return True

    # initialize the prime value to true
    prime = True

    # initialize the list of primes
    prime_list = []

    # loop through the string
    for char in string:
        # if the char is a letter, convert to ascii
        if char.isalpha():
            ascii_num = ord(char)
        # otherwise keep the char as is
        else:
            ascii_num = char
        # append the ascii number to the list of primes
        prime_list.append(ascii_num)
    # call is_prime on the sum of the prime list
    prime = is_prime(sum(prime_list))
    return prime
