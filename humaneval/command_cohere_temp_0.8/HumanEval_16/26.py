Here's the Python code to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set data structure to remove duplicate characters and ensures that the count is correct regardless of the case. 

Here's how you can use it in the context of a script that checks the function against the given test cases:
```python
def test_count_distinct_characters():
    # Test case 1
    assert count_distinct_characters('xyzXYZ') == 3

    # Test case 2
    assert count_distinct_characters('Jerry') == 4

test_count_distinct_characters()
```
This code uses the `assert` statement to perform a check against the function's behaviour with the given test cases. Ensuring that the code behaves as expected is crucial to avoiding errors and bugs.