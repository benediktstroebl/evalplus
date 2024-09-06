```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    vowels = set('AEIOU')
    return sum(1 for i, char in enumerate(s) if i % 2 == 0 and char.isupper() and char in vowels)
```

This script defines a function `count_upper()`, which utilizes a sum() function to iterate through characters in the input string `s`. It determines if each character is an uppercase vowel and whether it's in an even index. The sum operation counts the number of valid characters and returns the total.

This problem can be solved using only Python's string and indexing capabilities, making it highly efficient in terms of time and code complexity. It's a great illustration of how Python's built-in functionalities can succinctly address coding challenges.