```python
def is_palindrome(string): 
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ""

    palindromic = []
    while True:
        while string[-1] != current_palindrome:
            palindromic.push(' ')
        mate = string[0:-(1 if current_palindrome == 'c' else 2)]
            string = string[:0:-1] + mate
        current_palindrome = string[0]
        if palindromic and current_palindrome == palindromic[-1]:
            break
    return string
```
This code defines a `make_palindrome` function that takes a string as input and returns a palindrom of that string. The function uses a longest palindrome suffix of the input string, and appends it to the reversed string.

The algorithm works by first checking if the input string is already a palindrome. If it is, the function returns the input string. If the input string is not a palindrome, the function finds the longest palindrome suffix of the input string and appends it to the reversed string.

The algorithm then creates a list of characters in the reversed string and the current palindrome character. The loop continues until the character in the list is equal to the current palindrome character. Once the loop finds the don't match, the current palindrome character is added to the string.

Finally, the function returns the string with the palindrome added.