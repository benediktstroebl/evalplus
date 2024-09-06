```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

# Test the function
string1 = "xyzXYZ"
result1 = count_distinct_characters(string1)
print("Result1:", result1)

string2 = "jerry"
result2 = count_distinct_characters(string2)
print("Result2:", result2)
```