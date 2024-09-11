```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    :param string: Input string
    :return: Number of distinct characters in the string
    """
    # Convert the string to lowercase to ignore case sensitivity
    lower_case_string = string.lower()
    
    # Convert the string to a set to remove duplicate characters
    distinct_characters = set(lower_case_string)
    
    # Return the number of distinct characters
    return len(distinct_characters)

# Test cases
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4
```

This script works by first converting the input string to lowercase using the `lower()` method. This ensures that the same character in different cases is not treated as distinct. It then converts the string to a set, which automatically removes any duplicate characters because sets in Python cannot contain duplicate elements. The `len()` function is then used to return the number of elements in the set, which is equivalent to the number of distinct characters in the original string.