
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Write your code here
    def is_prime(n, i):
        if n == 1:
            return False
        if n % 2 == 0:
            return False
        for num in range(3, int(n**0.5) + 1, 2):
            if n % num == 0:
                return False
        return True

    string = string.upper()
    for i in range(1, len(string)):
        if string[i] == string[i-1] or string[i] == string[i-2] or string[i-1] == string[i-2]:
            continue
        if is_prime(int(string[i]), i) and is_prime(int(string[i+1]), i+1):
            return True
    return False

string = input("Enter a string: ")
