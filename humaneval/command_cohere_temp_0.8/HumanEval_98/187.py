```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    vowels = set('AEIOU')
    return sum(1 for i, char in enumerate(s) if i % 2 == 0 and char.isupper() and char in vowels)
```

The function `count_upper` takes a string as input and calculates the number of uppercase vowels in even indices. It does so by first creating a set containing all uppercase vowels, then iterating through the input string and counting the number of times the condition `i % 2 == 0` and `char.isupper()` and `char in vowels` are all satisfied, using the `sum` function to count the number of satisfies conditions. The specified test cases pass.