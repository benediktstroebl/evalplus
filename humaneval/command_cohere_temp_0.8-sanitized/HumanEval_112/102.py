def reverse_delete(s, c):
    # Resultant String after deletion
    result = [x for x in s if x not in c]

    # Checking if the resultant string is a palindrome
    # by comparing the first and last characters
    return (result, result[0] == result[-1])