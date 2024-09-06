```python
def max_element(l: list) -> int:
    """Return maximum element in the list."""
    return max(l)
```

This Python script defines a function called `max_element` that takes a list `l` as input and returns the maximum element in the list. The `max` function takes the list as an argument and returns its maximum element. 

This solution is concise and efficient, as it utilizes the built-in `max` function to find the maximum element, making it a crucial part of the Python Standard Library for such use cases. 

If you would like to test this script, you can create a file called `max_element_test.py` and add the following content to it:
```python
def test_max_element(l):
    assert max_element(l) == 3
    l=[1, 2, 3]
```

This will test the `max_element` function with a test case where the maximum element of a list is 3. 

To execute the test, you can run the following command:
```python
python test_max_element.py
```

This will run the test, and regardless of the programming language, the test will pass.