def reverse_delete(s, c):
    # Resultant string after deletion of characters in s that are equal to any character in c
    result = [x for x in s if x not in c]

    # Check if the remaining string is a palindrome
    return result + [True], result + [False]