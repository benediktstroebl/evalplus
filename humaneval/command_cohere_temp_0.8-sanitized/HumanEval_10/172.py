def make_palindrome(string: str) -> str:
    if not string:
        return string

    # Find the longest palindrome suffix in the string
    i = string.rfind(string[::-1])

    # If no palindrome suffix, simply return the string
    if i == -1:
        return string

    # Extract the palindrome suffix and reverse it
    palindrome_suffix = string[i:]
    reversed_prefix = palindrome_suffix[::-1]

    # Construct the result string by concatenating the original string
    # up to the palindrome suffix, the reversed prefix, and the rest of the string
    result = string[:i] + reversed_prefix + string[i+len(reversed_prefix):]

    # Return the constructed palindrome
    return result