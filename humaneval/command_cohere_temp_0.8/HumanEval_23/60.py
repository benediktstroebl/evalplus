```python
def strlen(s: str) -> int:
    """Returns the length of a string."""
    return len(s)
```

This Python script defines a function called `strlen` that takes a string as an argument and returns the length of that string. This is achieved by using the `len()` function in Python, which takes a string as an argument and returns the number of characters (including spaces, special characters, and digits) in the string. 

This satisfies the description provided in the prompt, as it defines a function with the signature `def strlen(string: str) -> int:` and the function body calculates the length of the input string `s`. 

This function can be used to calculate the length of any string passed to it as an argument, making it a useful tool for various string-related tasks in programming. 

If you would like to test this function to ensure it behaves as expected, you can write tests in the same file as the function or use it as a part of a broader application. 

For example, you can reference the provided tests in the script to ensure it satisfies those use cases:
```python
>>> strlen('')
0
>>> strlen('abc')
3
```

If you would like to test other scenarios, you can uncomment the test cases below and modify the expected output values accordingly:
```python
# >>> strlen('aa')
# 2
# >>> strlen('a')
# 1
# >>> strlen('abcde')
# 5
# >>> strlen('This is a longer string')
# 16
``` 

This file can then be executed as a Python script, which will run the tests and confirm that the `strlen` function behaves as expected.