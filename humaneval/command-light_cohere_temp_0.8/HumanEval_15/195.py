Here's a self-contained Python function that generates a sequence of numbers within a given range:
```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n} {" + str_sequence(n-1) + "}"

def str_sequence(n) -> str:
    return "".join(range(n))

#Test cases
assertEqual(string_sequence(0), '0')
assertEqual(string_sequence(5), '0 1 2 3 4 5')
assertEqual(str_sequence(6), '0 6 7 8 9')
```
This function uses a helper function `str_sequence` which generates a sequence of numbers within the range [0, n-1], where n is the argument passed to the function.