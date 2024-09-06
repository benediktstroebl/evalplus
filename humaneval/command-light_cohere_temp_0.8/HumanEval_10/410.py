Here is a Python script that contains a self-contained function to solve the problem of finding the shortest palindrome using the longest palindromic prefix:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ""

    # Find the longest palindromic suffix
    palindrome = find_palindrome(string)

    # Construct the palindrome by appending the palindromic suffix to the string
    return palindrome + string[::-1]

def find_palindrome(string):
    """ Find the longest palindromic suffix """
    char = string[-1]  # Get the last character
    for preceding_char in string[:-1]:
        if char == preceding_char:
            continue  # Same character, ignore
            break  # Move to next character
        if is_palindrome(string[preceding_char:]):
            return preceding_char
    return None

# Example usage
print(make_palindrome("at"))
```
This function uses a recursive approach to find the longest palindromic suffix. The main function make_palindrome takes a string as input and first checks if the input is empty. Then, it calls the find_palindrome to find the longest palindromic suffix. Finally, it constructs the string by appending the palindromic suffix to the string. The find_palindrome function uses a similar approach to find the longest palindromic suffix.