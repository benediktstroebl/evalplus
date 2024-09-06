Here's the code with a self-contained function that counts the distinct characters in a given string:
```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

# Test the function
def test():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('abc') == 3
    assert count_distinct_characters('JERRY') == 4
    assert count_distinct_characters('') == 0
    assert count_distinct_characters('I') == 1
    assert count_distinct_characters('hello world!') == 6
```
This code defines a function count_distinct_characters that takes a string as input and returns the count of distinct characters in the string. The function uses the particular to return the length of the set of characters in the string, which is equal to the number of distinct characters. The test function uses the test the function with various input strings and asserts that the output is correct. This allows us to verify that the count_distinct_characters function is working as expected.