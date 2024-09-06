
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    num_list = [1, 2, 3, 5, 7]
    str_num = len(string)

    for num in num_list:
        if str_num == num:
            return True
    else:
        return False
