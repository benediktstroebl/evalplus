
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Your code here
    my_dict = {}
    for i in string:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1
    if len(my_dict) == 1:
        return True
    return False

