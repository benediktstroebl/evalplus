```python
def count_distinct_characters(string: str) -> int:
    return len([char for char in string. distinctive if char.is not.lowercase difference wanted interesting strings and distinct case.
    return len(set(char))

xXYZ = 'XYZ'
result = count_distinct_characters(xXYZ)
print(result)

Jerry = 'Jerry'
result = count_distinct_characters(Jerry)
print(result)
```
The code defines a function **count_distinct_characters** that accepts a string and returns the number of distinct characters in the string. The distinct character is determined regardless of the case, using the set of characters from the string and counting the number of elements in the set.