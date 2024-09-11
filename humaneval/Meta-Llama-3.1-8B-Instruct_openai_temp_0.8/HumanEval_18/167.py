```markdown
### Problem: How Many Times
Find how many times a given substring can be found in the original string.
Count overlapping cases.

### Solution

```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to be searched.

    Returns:
        int: The number of times the substring can be found in the original string.
    """
    count = 0
    start = 0
    
    # Loop until the substring is not found in the string
    while True:
        # Find the index of the substring in the string starting from the current start index
        index = string.find(substring, start)
        
        # If the substring is not found, break the loop
        if index == -1:
            break
        
        # Increment the count and move the start index to the right of the found substring
        count += 1
        start = index + 1
    
    return count

# Example use cases
print(how_many_times('', 'a'))  # Output: 0
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
```

### Explanation

This script defines a function `how_many_times` that takes two arguments: `string` and `substring`. It uses a while loop to find all occurrences of the `substring` in the `string`, including overlapping cases. The `find` method is used to find the index of the `substring` in the `string` starting from the current `start` index. If the `substring` is found, the count is incremented and the `start` index is moved to the right of the found `substring`. The loop continues until the `substring` is not found in the `string`. The function returns the total count of occurrences of the `substring` in the `string`.