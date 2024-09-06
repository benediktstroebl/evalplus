```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 and ending at n-1 inclusive."""
    sequence = [0] + [x + 1 for x in range(n)] + [n]
    return "".join(sequence)

# Test cases
test_passes = [
    (0, ""),  
    (1, "1"),  
    (5, "0 5"), 
    (10, "0 9")
]

for i, test in enumerate(test_passes):
    result = string_sequence(test[0])
    assert result == test[1], f"TestCase {i+1}: Expected {test[1]}, but got {result}"
```  The code defines a function called `string_sequence` that takes an integer `n` as input and returns a string containing space-delimited numbers from 0 to n-1 inclusive. The function creates a sequence of numbers and returns it as a string, which is then compared to the expected string from the test case.