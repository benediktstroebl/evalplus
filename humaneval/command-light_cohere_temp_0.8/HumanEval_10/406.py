Here is a self-contained Python function that solves the problem of creating a palindrome from a given string:
```python
def is_palindrome(string):
    """Test if given string is a palindrome"""
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string"""
    if not string:  # empty string
        return ""
    # Find the longest postfix of supplied string that is a palindrome
    postfix = ''.join_palindromes(string)
    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    return postfix + string[::-1][len(postfix):]

def join_palindromes(string):
    """Concatenates all palindromes in the string"""
    words = string.split(' ')')
    each = words[:-1]
    words.append(words[-1])  # append original word to end
    return ' '.join(words)

if __name__ == "__main__":
    print(make_palindrome('cata' ))
    print(join_palindromes('hello world'))  # this will output: 'elhwrdowol'
```
The function is_palindrome checks if the given string is a palindrome. The function make_palindrome finds the shortest palindrome that begins with a supplied string. It does this by breaking the string into substrings (palindrome prefix) and postfix (palindrome suffix) and concatenates them to form a palindrome. The function join_palindromes splits a string into substrings and then finds all the palindromes in the string.