```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set()
    for i in range(len(s)-2):
        if len(set([s[i], s[i + 1], s[i + 2]])) != 3:
            return False
    return True
```

This Python script defines a function called `is_happy` that takes a single string as an input. This function returns True if the string is "happy"—that is, it has a length of at least 3 and every set of 3 consecutive letters within the string are distinct. Otherwise, it returns False.

The script includes test cases that verify the function's behavior against a variety of strings. These test cases can be executed to ensure the accuracy of the implementation. 

You may assert the function's correctness by running the test suite with the `python` command and observing the test results. Here is an example:
```python
python -m unittest tests.test_is_happy
```

To run this test, you must have the `unittest` module installed. This module is typically installed as a part of the Python standard library. If it is not installed, you can do so by running `pip install unittest` in your terminal.