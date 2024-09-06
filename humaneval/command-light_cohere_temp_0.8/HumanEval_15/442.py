```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n}{"*n+1}
    ```

This code defines a function called string_sequence that takes an integer n as input and returns a string containing n copies of the number 0, each separated by a space. The function uses the string formatting with f-strings and the **{}** syntax to create the desired output.