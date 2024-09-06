
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for num in prime_list:
        if string[0] == '2':
            if string[-1] == '2':
                continue
            if num % string[0] == 0:
                return False
        elif string[0] == '3':
            if num % string[0] == 0:
                continue
            if string[-1] == '3':
                continue
            if num % string[0] == num % string[1] == 0:
                return False
        elif string[0] == '5':
            if num % string[0] == 0:
                continue
            if string[-1] == '5':
                continue
            if num % string[1] == 0 or num % string[2] == 0:
                return False
        else:
            if num % string[0] == 0:
                continue
            for i in range(1, len(string)):
                if (num % string[i]) == 0:
                    return False
    return True