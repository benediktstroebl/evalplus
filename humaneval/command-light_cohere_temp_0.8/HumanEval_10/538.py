Here is a self-contained Python script that defines a function to solve the problem:
```python
def is_palindrome(string): 
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''

    # This is the core of the algorithm
    # We find the palindrome prefix and append the rest of reversed string 
    palindrome = string[0:min(len(string), len(reversed(string[1:]))]
    return palindrome + reversed(string[1:])

def test_make_palindrome():
    assert make_palindrome('') == ''
    assert make_palindrome('cat') == 'catac'
    assert make_palindrome('cata') == 'catac'

def main():
    test_make_palindrome()

if __name__ == "__main__":
    main()
```

This code defines a function `is_palindrome` that checks if a given string is a palindrome, and another function `make_palindrome` that constructs a palindrome given a string. The `test_make_palindrome` function verifies the output of the `make_palindrome` function for different test cases. 

Finally, the `main` function is used to execute these functions.