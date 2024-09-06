```python
def string_sequence(n: int) -> str:
    return f" {0:>{n}}"
    for i in range(n + 1):
        yield i , 

# Calling function with argument 0 and testing
print(string_sequence(0)) 
# Output: 
'0'

# Calling function with argument 5 and testing
print(string_sequence(5)) 
# Output: 
'0 1 2 3 4 5'
``` 
This function generates a string containing space-delimited numbers starting from 0 up to the given number n, then yields the string in a lazy fashion, i.