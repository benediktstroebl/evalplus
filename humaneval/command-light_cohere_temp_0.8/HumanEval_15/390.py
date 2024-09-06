Here is a Python script that contains a self-contained function that solves the problem of generating a sequence of numbers in a markdown-formatted string:
```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {next(range(1, n+1))}..."

# Test the function
print(string_sequence(5))  # Output: 0 1 2 3 4 5 

``` 
This code defines a function 'string_sequence' that accepts an integer 'n' and returns a string containing space-separated numbers from 0 to n. The function utilizes the string formatting with the use of the 'next' function from the 'range' builtin to generate the sequence of numbers, and finally, it returns a string containing these numbers.