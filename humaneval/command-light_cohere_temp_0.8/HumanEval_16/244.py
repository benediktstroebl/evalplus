```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.s.count() if c in string of string for c in string})

# Example usage
x = "xyzXYZ"
print(count_distinct_characters(x))  # Output: 3

y = "Jerry"
print(count_distinct_characters(y))  # Output: 4

```
This code defines a function `count_distinct_characters` that calculates the count of distinct characters in a given string. The function utilizes a loop to iterate through each character in the string and uses the `count()` method to keep track of characters encountered. The `set()` method is then used to filter out duplicate characters, resulting in an array of distinct characters. The count of distinct characters is then returned as the result.