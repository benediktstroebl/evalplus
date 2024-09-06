Here's a Python script that contains a function related to the task described in the code block provided:
```python
def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of """
    return len(set(string.lower()))
```
This function uses the `set` function to remove duplicate characters, and the `lower()` method to make the comparison case-insensitive. 
It can be tested as follows:
```python
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 4
    assert count_distinct_characters('Hello, hello!')) == 6
``` 
The test code provided above verifies the functionality of the `count_distinct_characters` function. It checks the output of the function against the expected result for three different inputs. 
The `assert` statement verifies that the output of the `count_distinct_characters` function is equal to the expected result. If the assertions pass, it means that the function works as intended.