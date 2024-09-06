def reverse_delete(s, c):
    # Resultant string after deletion of characters in s that appear in c
    result = ''.join(x for x in s if x not in c)
    # Check if the remaining string is a palindrome
    return result, result == result[::-1]