```python
def strlen(s: str) -> int:
    """Returns the length of a string."""
    return len(s)
```

This Python script defines a function named strlen that takes a string s as an argument and returns the length of that string. It utilizes the built-in Python function len to compute the number of characters in the given string. The function is aptly named strlen, following common convention, as it performs the task of determining the length of a string. 

This function is self-contained, meaning it does not rely on any external variables or functions to accomplish its task. It is a straightforward utility function that directly fulfills the request to return the length of a given string. 

To test this function, you can call it with different strings and verify that the returned lengths are correct. Here is an example:
```python
>>> strlen("Hello, World!")
13
>>> strlen("")
0
>>> strlen("abc")
3
```

This calls to strlen with different strings demonstrate the function's behavior and confirm its correctness. The tests check edge cases as well as normal scenarios, ensuring that the function behaves as expected in various contexts.  This thorough testing strategy ensures that the function behaves correctly and aligns with the problem statement.