
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
        if num == 1:
            return False
        if num == 2:
            return True
        counter = 2
        while counter < num:
            if num % counter == 0:
                return False
            counter += 1
        return True
            
    return len(string) == 1 or is_prime(len(string))
    