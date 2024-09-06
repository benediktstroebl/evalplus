```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c not c.isalpha()})
 using {c} for c in string if c not in string.isalpha()]
```. Using a set of characters, this function counts all distinct characters in the string, regardless of their case. This function is indeed self-contained and can be easily reused in various parts of the code that require character count.