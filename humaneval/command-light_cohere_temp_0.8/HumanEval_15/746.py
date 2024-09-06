```python
def string_sequence(n: int) -> str:
    return f"0 {n} 2 {n+1} 3 {n+2} 4 {n+3}"
    
# Test the function
print(string_sequence(0))  # Output: 0 
print(string_sequence(1))  # Output: 01
print(string_sequence(5))  # Output: 015 

```