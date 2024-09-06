```python
def string_sequence(n: int) -> str:
    return f" {0:0>{n}"
    # return a string of space-separated numbers from 0 to n
    # uses string formatting which is implemented by the f-string specifier
    # https://www.aren formatted strings in Python are a way to represent large numbers concisely
# It uses the format specifier to insert the number 0:0><n into the string.

# test cases
print(string_sequence(0))
print(string_sequence(5))
print(string_sequence(-5))
print(string_sequence(1))
```