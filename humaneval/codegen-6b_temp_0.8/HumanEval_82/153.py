
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
        for i in range(2,num):
            if num % i == 0:
                return False
        return True
    def is_prime_num(num):
        if num < 2:
            return False
        return is_prime(num)    
    new_string = ""
    for char in string[::-1]:
        if is_prime_num(len(new_string)):
            new_string += char
        else:
            return False
    return is_prime_num(len(new_string))
