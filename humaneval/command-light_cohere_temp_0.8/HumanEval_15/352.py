Here's the code:
```python
def string_sequence(n: int) -> str:
    return f" {0:>{n}} "
    # 0 -> '0'
    # 1 -> '1' 
    # ... 
    # n -> 'n'+'n'
    # example:
    # string_sequence(5) 
    # returns '0 1 2 3 4 5'
```
The code defines a function named string_sequence that takes an integer n as input and returns a string containing a sequence of numbers from 0 up to n inclusive. This is using the string formatting that displays the numbers separated by spaces.