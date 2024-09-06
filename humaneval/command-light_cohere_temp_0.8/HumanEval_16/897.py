```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

# Tests
string1 = "xyzXYZ"
assertEqual(count_distinct_characters(string1), 3)

string2 = "jerry"
assertEqual(count_distinct_characters(string2), 4)

# You can use this function in your markdown code block to solve the problem.