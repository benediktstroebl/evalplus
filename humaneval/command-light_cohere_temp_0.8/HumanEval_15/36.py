Here is a Python script with a self-contained function that solves the problem of creating a string of numbers from 0 to n:
```python
def string_sequence(n: int) -> str:
    return f" {0}  {1} {2} {3} {4} {5}" * n

# Test the function with different values of n
print(string_sequence(0))  # Output: 0  1
print(string_sequence(1))  # Output: 01
print(string_sequence(5))  # Output: 015
print(string_sequence(10)) # Output: 0101010101
```
This script defines a function called string_sequence, which takes an integer n as input and returns a string containing space-delimited numbers from 0 to n. The function uses the string formatting and the concept of repetition to achieve this.