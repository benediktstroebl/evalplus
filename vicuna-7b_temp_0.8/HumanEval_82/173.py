
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # check if the string is empty
    if len(string) == 0:
        return True

    # check if the string is '1'
    if len(string) == 1:
        return True

    # check if the string is a prime number
    # the function below checks if the remainder of the string divided by any number
    # between 2 and the square root of the length of the string is 1
    for i in range(2, int(len(string) ** 0.5) + 1):
        if remainder(string, i) == 1:
            return True
    return False

string = input("Enter a string to check: ")
