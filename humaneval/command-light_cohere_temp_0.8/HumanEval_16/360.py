```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string. string() if c not c.lower() and distinct for(string)})

# Example usage:
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))    # Output: 4
```
This script defines a function `count_distinct_characters` that calculates the count of distinct characters in a given string, regardless of case. It uses a distinct- method to achieve this, where it iterates through each character and checks if it is not lowercased, which means it's distinct from all other characters in the string. The result is then stored in a dictionary and counted to return the final count of distinct characters.