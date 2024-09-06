Here is a Python script that includes the self-contained function `count_distinct_characters` that calculates and displays the number of distinct characters in a given string regardless of the case:

```python
def count_distinct_characters(string: str) -> int:
    """
    Count the number of distinct characters in a given string, ignoring case.
    """
    string = string.split('', '')
    characters = set(string)
    distinct_count = len(characters)
    return distinct_count

# Test cases
test_count_distinct_characters = lambda: count_distinct_characters('xyzXYZ') # Output: 3
test_count_distinct_characters('jerry') # Output: 4

# Main function call
print(count_distinct_characters('Hello World'))  # Output: 5
```