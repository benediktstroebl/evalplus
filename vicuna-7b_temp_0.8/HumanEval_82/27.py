
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # initialize flag
    prime = True

    # loop through each character in the string
    for character in string:
        # check if the string length is divisible by 2
        if character == '2':
            prime = False
        elif character == '3':
            if string[0] == '3' and string[1] == '3':
                prime = False
        elif character == '5':
            if string[0] == '5' and string[1] == '5':
                prime = False
        elif character == '7':
            if string[0] == '7' and string[1] == '7':
                prime = False
        elif character == '11':
            if string[0] == '11' and string[1] == '11':
                prime = False
        else:
            # check if the string length is divisible by 3
            if string.count(character) % 3 == 0:
                prime = False
            # check if the string length is divisible by 4
            if string.count(character) % 4 == 0:
                prime = False
            # check if the string length is divisible by 5
            if string.count(character) % 5 == 0:
                prime = False
            # check if the string length is divisible by 7
            if string.count(character) % 7 == 0:
                prime = False

    return prime
