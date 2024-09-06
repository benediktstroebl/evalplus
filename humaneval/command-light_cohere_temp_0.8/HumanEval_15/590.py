```python
def string_sequence(n: int) -> str:
    return f" {0:0>{n}"

#Test the function:
print(string_sequence(0))  
print(string_sequence(1))  

#Test with large values:
print(string_sequence(10))
print(string_sequence(123))  

print(string_sequence(1000000))
```