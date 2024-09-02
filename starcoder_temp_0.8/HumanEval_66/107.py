
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
    # Check out the return statement in the editor. It checks if the string is empty. If it is, it returns 0.
    # If the string is not empty, the function iterates through each character in the string.
    # It checks if the character is an upper-case letter, and then it adds that character's ASCII value to a running total.
    # Finally, the function returns the sum of all the upper-case characters in the string.
    # Read the code below, then click "Test Run" to see how it will be tested and how your function will be run on the server.
    # After you are satisfied with your results, click "Submit".

    result = 0
    for i in s:
        if i.isupper():
            result += ord(i)

    return result

