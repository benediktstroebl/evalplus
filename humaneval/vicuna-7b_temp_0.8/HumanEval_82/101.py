
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Use a for loop to check if the length of the string is prime
    for num in range(2, len(string)):
        if string[0] == string[num]:
            return False
        if string[num-1] == string[num]:
            return False
    return True

string = input("Enter a string: ")
