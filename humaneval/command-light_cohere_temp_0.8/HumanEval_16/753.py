```python
def count_distinct_characters(string: str):
    return len(set(string.lower()))

x = "XYZ"
y = "Jerry"

print(count_distinct_characters(x))  # Output: 3
print(count_distinct_characters(y))  # Output: 4
```
The provided code defines a function `count_distinct_characters` that takes a string as input and counts the number of distinct characters regardless of their case. It achieves this by converting the string to lowercase using the `lower()` method and then creating a set of characters from that lowercase string. The number of distinct characters in the set is then returned as the result of the function.