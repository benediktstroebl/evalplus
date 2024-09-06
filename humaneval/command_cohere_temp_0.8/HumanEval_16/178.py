Here's the Python code with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct characters in the given string, regardless of case. It first converts the input string to lowercase to ensure that characters are treated as identical regardless of case and then counts the number of characters by converting the set into a list and using the `len()` function. 

Here's an example of how to use it in a Python script to execute the function on different input strings and parse the output:
```python
def test_count_distinct_characters():
    string1 = 'xyzXYZ'
    string2 = 'Jerry'
    assert count_distinct_characters(string1) == 3
    assert count_distinct_characters(string2) == 4
```
The function can now be used to accept a string as input and return the number of distinct characters in the string.