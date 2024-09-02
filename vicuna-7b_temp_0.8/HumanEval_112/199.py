
def reverse_delete(s,c):
    """Task
    We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    Example
    For s = "abcde", c = "ae", the result should be ('bcd',False)
    For s = "abcdef", c = "b"  the result should be ('acdef',False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)
    """
    # Check if the s is empty
    if len(s) == 0:
        return '', False

    # Check if the c is empty
    if len(c) == 0:
        return s, False

    # Check if the s is a palindrome
    rev_s = rev_string(s)
    if rev_s == s:
        return s, True

    # Create a dictionary to count the number of occurrences of characters in s
    count = {}
    for char in s:
        count[char] = count.get(char,0) + 1

    # Loop through the characters in c
    for char in c:
        # If the character is not in the dictionary, increment the count
        if char not in count:
            count[char] += 1
        # Remove the character from the dictionary
        del count[char]

    # Loop through the characters in s
    result = ''
    for char in s:
        # If the character is not in the dictionary, remove it from s
        if char not in count:
            s.remove(char)
        else:
            # If the count of the character is 0, remove it from s
            if count[char] == 0:
                s.remove(char)
        # Add the character to the result
        result += char
    return result, False
