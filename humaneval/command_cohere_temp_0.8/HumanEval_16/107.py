Here's the Python code with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store unique characters in the provided string, regardless of case, and then returns the count of these distinct characters.

Here's how you can use it and provide tests:
```python
def test_count_distinct_characters():
    # Test case 1
    assert count_distinct_characters('xyzXYZ') == 3
    # Test case 2
    assert count_distinct_characters('Jerry') == 4 

test_count_distinct_characters()
```
The test module will ensure that the function `count_distinct_characters` accurately counts distinct characters. 
The syntax `assert 4 == 4` is used to check if both values are equal.  In case of inequality, the `assert` will raise an `AssertionError`, signaling that the test has failed. 
The tests are placed after the function definition so that you can quickly identify any issues and debug the code. 
The `count_distinct_characters` function is designed to handle various strings and provide the correct count of distinct characters, ensuring readability and efficiency. 
It can be directly called to test different scenarios. 
To execute the test suite, simply add this code to a Python file and run the file. This approach provides a comprehensive and organized way to address the problem and verify the correctness of the solution.