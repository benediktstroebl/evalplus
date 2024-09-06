Here's a self-contained Python function that generates a sequence of numbers in a markdown-formatted string:
```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    
    # Initialize string with blank spaces
    result = ""

    # Add numbers 0 to n inclusive
    for i in range(n):
        result += str(i+1) + " "

    return result

# Test cases
test_seq = [
    assert string_sequence(0) == "0",
    assert string_sequence(1) == "1",
    assert string_sequence(5) == "0 1 2 3 4 5"
]
```

This code defines a function `string_sequence` which returns a string containing space-separated numbers from 0 to n. It's then tested with various input sizes using a test case block.  The results of the function call are expected to match the provided test cases.