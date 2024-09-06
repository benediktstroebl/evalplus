Here's a self-contained Python script with a function that calculates the count of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string if c.isupper(string)})

# Test case 1
test_case1 = "xyzXYZ"
assert count_distinct_characters(test_case1) == 3

# Test case 2
test_case2 = "jerry"
assert count_distinct_characters(test_case2) == 4

# Test case 3
test_case3 = "jduct | kleen"
assert count_distinct_characters(test_case3) == 5
```
This script defines a function `count_distinct_characters` that calculates the number of distinct characters in a given string. By using a use of the string.isupper method, it converts all characters to uppercase before performing a set difference operation with the entire string, resulting in all distinct characters. The final count of distinct characters is then returned.