Here's the Python script with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct characters in the string after converting all characters to lowercase. This ensures that characters like 'x' and 'X' are treated as the same character. Finally, it returns the length of the set, which is the number of distinct characters. The unit tests provided as part of the problem statement are straightforward and can be implemented as: 
 ```python
def test_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 4
``` 
Running these tests using a testing framework like `pytest` would verify that the function behaves as expected. 
For more complex problems or larger code snippets, I can help you break down the problem into manageable tests and develop the solution iteratively. Feel free to provide more details or specifics, and I'll assist you in designing test cases and crafting the solution accordingly. Fiddling with the parameters and test inputs can be insightful, here are some additional tests you may want to include:
```python
test_distinct_characters()
# Test with an empty string.
assert count_distinct_characters('') == 0

# Test with a longer string.
string = ' alphabetsABCdefgJKLmnopQRstuvwxyz'
assert count_distinct_characters(string) == 26

# Test with a string containing only one character.
assert count_distinct_characters('xxxxxx') == 1

# Test with a string containing digits only.
string = '12344321'
assert count_distinct_characters(string) == 10
```