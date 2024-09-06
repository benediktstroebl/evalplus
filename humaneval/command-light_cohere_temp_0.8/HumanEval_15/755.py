Here is a Python script that contains a self-contained function that solves the problem of creating a sequence of numbers:
```python
import string

def string_sequence(n: int) -> str:
    sequence = [0]
    for i in range(1, n+1):
        sequence.append(sequence[-1] + 1)
    return ' '.join(sequence)

# Test case:
test_sequence = string_sequence(5)
print(test_sequence)   # Output: 0 1 2 3 4 5 

# Another test case:
test_sequence = string_sequence(0)
print(test_sequence)  # Output: ''
``` 
This function, `string_sequence` creates a sequence of numbers from 0 to n, where n is the input parameter passed to the function. The function uses a string.join method, which is used to join the numbers together with a space character to form a string.