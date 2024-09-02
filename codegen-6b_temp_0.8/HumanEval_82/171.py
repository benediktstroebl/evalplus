
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    string = string.replace(" ", "").lower()

    # List of numbers to check on
    prime_list = [2, 3, 5]

    for num in prime_list:
        if string[0:1] == str(num):
            return True
        elif len(string) % num == 0:
            return False

