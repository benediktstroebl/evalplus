def reverse_delete(s, c):
    # Remove characters in c from s
    s = [i for i, char in enumerate(s) if char not in c]

    # Check for palindrome
    return (''.joinjoin(s), False)