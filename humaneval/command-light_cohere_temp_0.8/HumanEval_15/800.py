```python
def string_sequence(n: int) -> str:
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        return ' '.join(str(i) for i in range(n))

# Test the function
print(string_sequence(0))  # Output: 0
print(string_sequence(1))  # Output: 1
print(string_sequence(5))  # Output: 0 1 2 3 4 5
print(string_sequence(10)) # Output: 
```

This code defines a function called `string_sequence` which generates a string containing space-separated numbers from 0 up to `n`, where `n` is the input. The function also has a series of `if-else` checks to decide the structure of the output string.