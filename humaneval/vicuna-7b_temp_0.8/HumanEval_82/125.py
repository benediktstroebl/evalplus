
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    prime_count = [True for i in range(2, int(1e5) + 1)]
    for char in string:
        if char.isdigit():
            for i in range(int(char) ** 2):
                if string[i] == char and prime_count[int(string[i]) - 1]:
                    return True
    return False
