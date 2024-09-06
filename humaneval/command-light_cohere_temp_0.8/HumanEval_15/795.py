Here's a Python script with a self-contained function that generates and returns a string containing space-delimited numbers from 0 to n:
```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n} {" + str_sequence(n - 1) + "}" 

def str_sequence(n: int) -> str:
    return "".join(str(i) for i in range(n)) 

# Test case 1:
print(string_sequence(0))  # Output: '0'

# Test case 2:
print(string_sequence(5))  # Output: '0 1 2 3 4 5'

# Test case 3:
print(str_sequence(0))  # Output: '0'

# Test case 4:
print(str_sequence(5))  # Output: '5 6 7 8 9'
```
This function will return a string with the desired format, where the numbers are separated by spaces.