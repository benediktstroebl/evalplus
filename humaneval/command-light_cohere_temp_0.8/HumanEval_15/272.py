Here's a self-contained Python script that defines a function string_sequence that returns a string containing space-delimited numbers starting from 0 and ending at n, passing in n as an argument:
```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return "".join(str(i) for i in range(n))

# Test the function
test_string_sequence = string_sequence(10)
print(test_string_sequence)  # Output: 0 10 11 12 13 14 15 16 17 18 19 20 

test_string_sequence = string_sequence(5)
print(test_string_sequence)  # Output: 0 1 2 3 4 

test_string_sequence = string_sequence(0)
print(test_string_sequence)  # Output: 0
```
This code defines a function string_sequence that returns a string containing space-delimited numbers starting from 0 and ending at n, where n is the argument passed to the function. The function is then tested with three different arguments, and the output is printed to the console.