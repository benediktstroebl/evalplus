A Python function that generates the shortest palindrome using the provided algorithm:
```python
def make_palindrome(string):
    # Find the longest postfix of supplied string that is a palindrome
    max_palindrome = ''
    for palindrome in string:
        if palindrome == palindrome[::-1]:
            max_palindrome = palindrome
    if len(max_palindrome) > len(string):
        return string + max_palindrome[::-1]
    else:
        return max_palindrome
```
This algorithm works by first identifying the longest palindrome substring in the input string. 

If this length is greater than the length of the original string, we can simply append the palindrome to the end of the string to create the desired palindrome. 

Otherwise, we search for the longest palindrome in the input string.