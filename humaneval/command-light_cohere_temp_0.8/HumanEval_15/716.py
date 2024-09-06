Here's the self-contained Python script with a function that creates a sequence of numbers in a markdown code block: 

```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive""" 
    return f"0 {n} 1 {n+1} 2 {n+2} 3 {n+3} 4 {n+4}"

# Example usage: 
print(string_sequence(5))  # Output: 0 5 6 7 8 9 10 

# Test cases: 
    assert string_sequence(0) == '0' 
    assert string_sequence(1) == '1' 
    assert string_sequence(5) == '0 1 2 3 4 5' 
    assert string_sequence(10) == "0 10 9 8 7 6 5 4 3 2 1" 
```