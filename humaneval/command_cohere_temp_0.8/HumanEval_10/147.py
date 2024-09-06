Here's a Python script with a self-contained function that solves the problem using Markdown code blocks:
```python
def is_palindrome(string: str) -> bool:
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    if not string:
        return string

    # Find the longest palindromic suffix
    i = string.rfind(|palindize|string[::-1])
    
    # Extract the reverse of the prefix before the palindromic suffix
    prefix = string[:i]
    palindic_suffix = string[i:]
    
    # Construct the shortest palindrome by concatenating the reverse of the prefix and the original palindic suffix
    return f"{prefix[::-1]}{palindic_suffix}"

# Helper function to convenience the find_palindromic_suffix calculation
def palindize(string: str) -> str:
    return string[::-1]
```

This script includes a helper function `palindize` facilitating the calculation of the reverse of a string in the `find_palindromic_suffix` calculation. 

The `make_palindrome` function first checks if the supplied string is empty, and returns it directly if so. Assuming the string is not empty, the function then finds the longest palindromic suffix of the string using the `find_palindromic_suffix` calculation. 

Next, the function extracts the reverse of the prefix before the palindromic suffix. The palindic suffix is then concatenated with the reverse of the prefix to construct the shortest palindrome. The result is returned as a string. 

This solution has a time complexity of `O(n)` wherein `n` is the length of the input string, and a space complexity of `O(1)`.