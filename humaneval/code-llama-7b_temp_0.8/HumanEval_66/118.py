
def digitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """

    # needs to have a variable for sum and a variable for current character.
    # variable for the sum starts at 0.
    # variable for current character starts at the first position in the string.
    # make a while loop
        # inside the while loop, make an if statement that checks if current character is an upper case letter.
            # if it is an upper case letter, add the ascii code of the letter to the sum.
        # make an if statement that checks if current character is a lower case letter.
            # if it is a lower case letter, don't do anything.
        # make an else statement.
            # if it is anything else, raise an error.
        # make the current character variable be the next position in the string.
    # return the sum.

    sum = 0
    current_character = 0
    while current_character < len(s):
        if s[current_character].isupper():
            sum += ord(s[current_character])
        elif s[current_character].islower():
            pass
        else:
            raise ValueError("Invalid Input")
        current_character += 1
    return sum
