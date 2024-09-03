```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive""" 
    return f"0 {n} {" + str(n + 1) + "}" * (n + 1)

# Test case 1: Verify function with different input values
print(string_sequence(0))  
print(string_sequence(1))  
print(string_sequence(5))  

# Test case 2: Verify return value for different n values
print(string_sequence(10))
print(string_sequence(11))
print(string_sequence(12))  

# Test case 3: Input validation error 
try:
    string_sequence(-1) 
except TypeError as e: 
    print(f"Error: Input must be a positive integer" , e)
```