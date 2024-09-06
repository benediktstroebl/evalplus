```python
def string_sequence(n: int) -> str:
    """ 
    Returns a string containing space-delimited numbers starting from 0 upto n inclusive. 
    """ 
    if n <= 0:
        raise ValueError("n must be a positive integer")
    string = "0"
    while n > 0:
        n -= 1
        string += str(n)
    return string

#test cases
test_sequence = string_sequence
test_sequence(0)
# expect output: '0'
test_sequence(1)
# expect output: '0 1'
test_sequence(5)
# expect output: '0 1 2 3 4 5'
test_sequence(-5)
# expect output: ValueError: n must be a positive integer
```