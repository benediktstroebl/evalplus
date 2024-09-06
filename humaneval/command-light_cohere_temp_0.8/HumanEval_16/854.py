```python
def count_distinct_characters(string: str):
    return len(set(string))

# Tests
string1 = "xyzXYZ"
assertEqual(count_distinct_characters(string1), 3)

string2 = "jerry"
assertEqual(count_distinct_characters(string2), 4)

# Use this function and pass a string to it
result = count_distinct_characters("Hello World")
print(result)
```