```python
def string_sequence(n: int) -> str:
    """ 
    Returns a string containing space-delimited numbers starting from 0 upto n inclusive.

    Args: 
        - n (int): total number of numbers to generate the sequence
    
    Returns: 
        - string: string of numbers generated 
    """
    return f"0 {n}{" * n

# test the function
print(string_sequence(0))
print(string_sequence(5))
print(string_sequence(-1))
print(string_sequence(10))
```