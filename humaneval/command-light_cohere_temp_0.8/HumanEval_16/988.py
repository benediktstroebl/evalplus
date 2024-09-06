```python
def count_distinct_characters(string: str) -> int:
    """
    Returns the number of distinct characters in the string, regardless of case.
    """
    string = "xyzXYZ jerry"
    # remove all non-alphphanumeric and space characters, keeping only letters
    characters = ''.join(char for char in string if char.isalpha(char) or  or char.isalpha(char)
    then

    return len(set(characters)))
    """

# test the function
print(count_distinct_characters('xyzXYZ jerry'))  # expected output: 4
print(count_distinct_characters('abc123'))  # expected output: 4
print(count_distinct_characters(' abilities'))  # expected output: 5
```