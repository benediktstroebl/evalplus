```markdown
### Counting Distinct Characters in a String
#### Problem Statement
Given a string, find out how many distinct characters (regardless of case) does it consist of.

#### Solution
```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of.
    
    Args:
        string (str): The input string.
    
    Returns:
        int: The number of distinct characters in the string.
    
    Examples:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry')
        4
    """
    # Convert the string to lowercase to ignore case sensitivity
    lower_case_string = string.lower()
    
    # Convert the string into a set, which automatically removes duplicates
    # Since sets only contain unique elements, the size of the set will be the number of distinct characters
    distinct_characters = set(lower_case_string)
    
    # Return the number of distinct characters
    return len(distinct_characters)

# Example usage:
print(count_distinct_characters('xyzXYZ'))  # Outputs: 3
print(count_distinct_characters('Jerry'))  # Outputs: 4
```

#### Explanation
This script defines a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters in the string. To ignore case sensitivity, the string is converted to lowercase before counting the distinct characters. This is achieved by using the `lower` function.

The script then uses a set to automatically remove duplicates from the string. Since sets only contain unique elements, the size of the set will be the number of distinct characters.

The function returns the length of the set, which represents the number of distinct characters.

Finally, the script includes example usage of the function to demonstrate its usage.