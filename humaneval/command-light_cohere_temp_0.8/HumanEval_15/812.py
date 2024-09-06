```python
def string_sequence(n: int) -> str:
    if not n:
        return 'Invalid input.

    start = 0
   
    end = n
    result = []
    while start < end:
        result.append(f"{start:02d}".start += 1
    return " ".join(result)

# Test cases
test_cases = [
    0, 
    5, 
    10, 
    "hello", 
    20  
 ]

for _ in test_cases:
    actual = string_sequence(_)
    assert actual == "".joinof([f"{n:02d}" for n in _]), "Expected: {!joinActual}"
```  Output should be a string containing space-separated numbers starting from 0 to n, or an error message if the input is not valid.