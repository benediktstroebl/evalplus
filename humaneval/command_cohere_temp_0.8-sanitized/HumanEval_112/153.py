def reverse_delete(s, c):
    # Resultant string after deletion of characters in s that are equal to any character in c
    result = [char for char in s if char not in c]

    # Check if the resultant string is a palindrome
    return (''.join(result), result == result[::-1])