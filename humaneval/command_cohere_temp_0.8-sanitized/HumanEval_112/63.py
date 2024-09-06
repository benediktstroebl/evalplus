def reverse_delete(s, c):
    # Resultant string after deletion of characters in s that are equal to any character in c
    result = [char for char in s if char not in c]

    # Check if the remaining string after deletion is a palindrome
    # By checking the length of the string after deletion,
    # if it is equal to the length of the string before deletion, it is a palindrome
    return result, len(result) == len(s)