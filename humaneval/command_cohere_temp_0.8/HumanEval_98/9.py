```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    import re

    pattern = re.compile(r'[EO]+')
    return sum(1 for _ in pattern.finditer(s)) // 2
```

The above code uses a regular expression and its finditer method to detect matches in the string s, then it sums up the matches and divides by 2 to obtain the number of uppercase vowels in even indices. Ultimately, it returns the final count. This approach allows the code to be concise and efficient while solving the problem.