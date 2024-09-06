```python
def add(x: int, y: int):
    return x + y
```
```python
>>> add(2, 3)
5
>>> add(5, 7)
12
```
```python
# Test Suite for add function
def test_add():
    assert add(2, 3) == 5
    assert add(5, 7) == 12
```

This code snippet includes the `add` function, test cases, and a test suite using the `pytest` framework. The function simply adds two numbers. The test cases verify the function's correctness against expected output. The test suite executes the test cases and reports any failures or errors, ensuring the function's reliability. 
The three code blocks are separated by a double line break, and the Markdown code fence continues until the end of the code block.