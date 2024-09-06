Here's a Python script with a self-contained function that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters_set = set(string.lower())
    return len(characters_set)
```
The function `count_distinct_characters` accepts a string as an argument and determines the number of distinct characters, case-insensitively, by converting the input string to lowercase and then counting the unique characters using a `set`. The output is then returned as an integer. 

To ensure the functionality, here is a test case:
```python
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 4
    assert count_distinct_characters('Hello, world!') == 6
    assert count_distinct_characters('...') == 3
```
The test case ensures the function performs correctly for a variety of inputs. 
To execute the test cases, run the following command in the same file:
```python
test_count_distinct_characters()
```
The `count_distinct_characters` function should provide you with the number of unique characters in any given input string, regardless of case, in a clear and reproducible manner.