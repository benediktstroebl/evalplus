Here's the Python script with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct characters in the string after converting all characters to lowercase. This ensures that characters like 'x' and 'X' are considered the same. The function then returns the length of this set, which is the number of distinct characters in the string.

To test this function, you can run the following code:
```python
test_cases = [
    ('xyzXYZ', 3),
    ('Jerry', 4),
    (# Tests with none printable characters
     '\n', 1),
     ('pears\napples', 2),
    (# Tests with diacritic characters 
     'jérôme', 3),
]

for inp, out in test_cases:
    assert count_distinct_characters(inp) == out
```
This will run the function `count_distinct_characters` on the input test cases provided in the `test_cases` list, and compare the output with the expected output provided in the `out` list. 

Let me know if you need anything else!