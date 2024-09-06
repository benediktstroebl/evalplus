Here's the solution to the problem using Python:
```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''

    palindrome = string[:0: int(len(string) ** 0.5)]
    initial_palindrome = palindrome + string[-1:]
    return initial_palindrome
```
The function 'make_palindrome' finds the shortest palindrome that begins with the supplied string. It iterates on the algorithm idea and utilizes the 'is_palindrome' function to check if the current part of the string is a palindrome.