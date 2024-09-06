
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # re = r"\d+"
    # new_string = re.findall(string)
    # if int(new_string[0]) > 1:
    #     for i in range(2, int(new_string[0])):
    #         if int(new_string[0]) % i == 0:
    #             return False
    # return True
    string = str(string)
    if len(string) > 1:
        for i in range(2, len(string)):
            if len(string) % i == 0:
                return False
        return True
    return False
    # return True if len(string) > 1 and all(string % i for i in range(2, len(string))) else False

