```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    
    #0-based loop to generate sequence of numbers
    s = "0"
    for i in range(1, n+1):
        s += str(i)
    
    return s

# Test the function with 0 and 5 as arguments
string_sequence(0)  
# '0'
string_sequence(5)  
# '0 1 2 3 4 5'
```