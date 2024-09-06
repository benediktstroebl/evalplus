
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # your code here

    # test case
    string_list = ['Hello', 'abcdcba', 'kittens', 'orange', 'apple']
    for string in string_list:
        if len(string) > 2:
            if len(string) % 2 != 0 and len(string) % 3 != 0:
                return True
    return False