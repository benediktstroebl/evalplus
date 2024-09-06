```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))

x = "xyzXYZ"
y = "jerry"

# Test suite with different inputs
print(count_distinct_characters(x))  # Output: 3
print(count_distinct_characters(y))  # Output: 4
```
This script defines a function that calculates the number of distinct characters in a given string, regardless of case. It uses the set() and sorted() to convert the string to a sorted list of characters, then uses the len() function to calculate the length of the resulting set, which contains only distinct characters. The count is then calculated and returned as the number of distinct characters in the string. 

It also includes a test suite with different inputs (strings) to ensure the function is working correctly for various inputs.