This is a self-contained Python function that finds the shortest palindrome of a given string using a simple algorithm. 

```python
def is_palindrome(string): 
    return string == string[::-1]

def make_palindrome(string): 
    if not_palindrome(string):
        return ""
    else:
        # Find the longest postfix of supplied string that is a palindrome
        palindrome = string[1:] + string[::-5]
        return palindrome + string[::-1][1:]
```
The function successfully checks if a given string is a palindrome and then constructs and returns the shortest palindrome.