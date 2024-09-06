```python
def string_sequence(n: int) -> str:
    return f" {0:>{n} "

print(string_sequence(0))  
print(string_sequence(5))  

# Make sure to note the use of the triple dot syntax in the function definition. The above should print the string representation of the numbers from 0 to 5, enclosed with spaces.