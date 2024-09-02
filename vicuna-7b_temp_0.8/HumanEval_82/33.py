
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Check for prime numbers under 10
    for num in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
        if string[0] == num or string[0] == "0" * (len(num) + 1) % 1000000 or string[0] == "0" * (len(num) + 1) % 1000000 or string[0] == num + "0" * (len(num) + 1) % 1000000:
            return False
        elif string[0] == num + "0" * (len(num) + 1) % 1000000 or string[0] == "0" * (len(num) + 1) % 1000000 or string[0] == num * 1000000 + "0" * (len(num) + 1) % 1000000:
            return False
        elif string[0] == num * 1000000 + "0" * (len(num) + 1) % 1000000 or string[0] == "0" * (len(num) + 1) % 1000000 or string[0] == num * 1000000 + "0" * (len(num) + 1) % 1000000:
            return False
        elif string[0] == num * 1000000 + "0" * (len(num) + 1) % 1000000 or string[0] == "0" * (len(num) + 1) % 1000000 or string[0] == num * 1000000 + "0" * (len(num) + 1) % 1000000:
            return False
        elif string[0] == num * 1000000 + "0" * (len(num) + 1) % 1
