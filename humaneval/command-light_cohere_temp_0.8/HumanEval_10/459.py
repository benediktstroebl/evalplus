A solution is a Palindrome Generator function that uses a helper function to achieve this.

```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(input_str):
    if not_palindrome(input_str):
        return input_str
    
    palindrome = []
    while True:
        palindrome.append(input_str[1])
        i = 2
        while i < len(input_str) - 1:
            if is_palindrome(input_str[i:i+1]):
                break
            i += 1
        else:
            palindrome.append(input_str[::-1])
    
    return ''.join(palindrome)

```

This function starts with an empty list and iterates over the characters of the input string. Then, it checks if the string from the beginning to the current character is a palindrome. If it is, it appends the character to the list. Otherwise, it appends the reverse of the character to the list.