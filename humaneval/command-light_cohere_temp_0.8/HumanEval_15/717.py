```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n} {n+1} {n+2} {n+3}"

# Test the function
test_str = string_sequence(5)
print(test_str)  

test_str = string_sequence(0)
print(test_str)

test_str = string_sequence(-5)
print(test_str)  

test_str = string_sequence(10)
print(test_str)
```