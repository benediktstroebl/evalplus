Here is a Python script that defines a self-contained function to generate a sequence of numbers in a markdown code block:
```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    
    # Base case
    if n == 0:
        return '0'

    # Initialize counter and string builder
    counter = 0
    string_builder = str()

    # Generate numbers up to n
    while counter < n:
        string_builder += str(counter)
        counter += 1

    # Return the constructed string
    return string_builder
```

This code is a self-contained solution that provides a function string_sequence that returns a string containing space-separated numbers starting from 0 up to the given integer n.