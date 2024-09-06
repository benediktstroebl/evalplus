```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n}..."join(str(i+1) for i in range(n))

# Test case 1: Basic function call
print(string_sequence(0))
# Prints: 0

# Test case 2: Function call with argument 5
print(string_sequence(5))
# Prints: 0 5 

# Test case 3: Negative arguments
try:
    print(string_sequence(-10))
except TypeError:
    print("Function did not accept negative argument")

# Test case 4: Large n argument
print(string_sequence(10000))
# Prints: 
```

200 100300 700 400 200 000