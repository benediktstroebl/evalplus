
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # code to check if the string is prime or not
    if len(string) > 2:
        for i in range(2, len(string)):
            if string[i] == string[i-1]**2 or string[i] == 1 or string[i] == 0:
                return False
        return True
    else:
        return True

if __name__ == '__main__':
    print(prime_length('Hello'))