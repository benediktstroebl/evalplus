def reverse_delete(s, c):
    # Resultant String after deletion
    result = [x for x in s if x not in c]
    # Check if the resultant string is a palindrome
    # By concatenating the reversed string to itself
    if result == result[::-1]:
        return ''.join(result), True
    else:
        return ''.join(result), False