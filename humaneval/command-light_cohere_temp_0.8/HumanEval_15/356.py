```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive."""
    return f"0 {n} {" + str(n+1) + "}" * (n+1)

#Test the function
test_string = string_sequence(10)
print(test_string)
```