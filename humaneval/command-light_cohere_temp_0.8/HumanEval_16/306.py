Here is a self-contained Python script with a function that solves the problem of counting distinct characters in a given string:
```python
def count_distinct_characters(string):
    """
    Count the number of distinct characters in a given string, ignoring case.
    Args: 
        string: str, the input string to check
    Returns: 
        int, the number of distinct characters
    """
    # Create a set of characters from the input string, removing duplicates and lowercasing
    distinct_chars = set(string.isupper())
    final_count = len(distinct_chars)
    return final_count

# Unit tests
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('jerry') == 4

# Main execution 
if __name__ == "__main__":
    test_count_distinct_characters()
```

This code provides a function `count_distinct_characters` that accepts a string as input and returns the count of unique characters in that string, regardless of case. The function uses a set to store the characters, which removes duplicates and converts everything to uppercase. Finally, it calculates the count of distinct characters and returns it. The function is then tested with two test cases: counting the number of distinct characters in 'xyzXYZ' and 'jerry'.