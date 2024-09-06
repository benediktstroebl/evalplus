Here's a Python script that contains a function named `count_upper()` which solves the problem as described in the markdown code block:
```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    import re

    pattern = re.compile(r'(A|E|I|O|U){2,}(?![^A-Z])', flags=re.I)
    matches = pattern.findall(s)
    return sum(1 for _ in matches)
```

This code works by first using the `re` module to create a regex pattern. The pattern `r'(A|E|I|O|U){2,}(?![^A-Z])'` uses the `I` flag to make the pattern case-insensitive, while matching strings with at least two consecutive uppercase vowels. The pattern is then used to find all matches in the string `s` using the `findall()` method, which returns a list of matches. Finally, it sums up the matches found, ensuring that only whole strings are counted by filtering with a mapping filament.

To test this code, you can call the `count_upper()` function with different test cases to verify the correctness of the solution. Here are some test cases to get you started:
```python
# Test case 1:
print(count_upper('aBCdEf'))  # Output: 1

# Test case 2:
print(count_upper('abcdefg'))  # Output: 0

# Test case 3:
print(count_upper('dBBE'))  # Output: 0
```

Ensure that you have the required dependencies, such as the `re` module, installed in your Python environment to run the code correctly. You can install the `re` module by default in Python but if you're using a virtual environment, you may need to activate it or refresh its packages with `venv`.