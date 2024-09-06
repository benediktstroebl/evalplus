
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
    prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for num in prime_list:
        if string[0] == num or string[0] == '0' and string[1] in (num, '1'):
            for i in range(1, len(string)):
                if string[i] == '0' and num not in (string[i-1], string[i-2]):
                    break
                elif string[i] % num == 0:
                    return False
            return True
    return False