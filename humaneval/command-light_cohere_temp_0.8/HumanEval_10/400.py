A solution for the problem is:
```python
def is_palindrome(string): 
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''

    # Find the longest palindrome from prefix.
    longest_palindrome = 0
    palindrome = ''
    for char in string:
        if is_palindrome(char):
            palindrome += char 
            if len(palindrome) > longest_palindrome:
                longest_palindrome = len(palindrome)
        else: 
            palindrome = char if palindrome == '' else palindrome + char

    # Append the reverse of the palindrome as suffix
    return palindrome + palindrome[::-1]
```

This solution works by first checking if the given string is a palindrome. If not, it returns an empty string. Then, it iterates through the string and checks each character to see if it's a palindrome. If it is, it appends the character to the beginning of the 'palindrome' variable. If the character is not a palindrome, it simply appends the character to the 'palindrome' variable. 

Finally, it appends the 'palindrome' variable reversed as the final suffix of the string, which gives the desired result.