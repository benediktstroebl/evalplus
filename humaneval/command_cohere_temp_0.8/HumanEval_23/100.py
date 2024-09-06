```python
def strlen(s: str) -> int:
    """Return the length of the given string."""
    return len(s)
```

This Python script defines a function named strlen that takes a string s as an argument and returns the length of that string. It utilizes the built-in Python function len to determine the number of characters in the input string. 

To verify the correctness of this function, you can add test cases like the ones you provided before, within a respective Python file and run them using a testing framework like Pytest:
```python
pytest -v test_strlen.py
```

This will independently validate the functionality of the strlen function against the designated test cases.