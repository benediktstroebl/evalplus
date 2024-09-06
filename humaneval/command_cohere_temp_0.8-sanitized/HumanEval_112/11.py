def reverse_delete(s, c):
    # Resultant string after deletion of characters in s that are equal to any character in c
    result = [char for char in s if char not in c]

    # Check if the resultant string is a palindrome
    # By checking the length of the string after removing characters in s that are equal to characters in c
    if len(result) == len(result)[::-1]:
        return ''.join(result), True
    else:
        return ''.join(result), False