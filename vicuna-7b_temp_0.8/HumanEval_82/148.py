
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
    for i in range(2, len(string)):
        if string[i] == '1':
            for j in range(i+1, len(string)):
                if string[j] == '1':
                    break
                if string[j] % 2 != 0 or string[j] % 3 != 0:
                    return False
                break
        elif string[i] % 2 != 0:
            return False
    return True

string = input("Enter string: ")
