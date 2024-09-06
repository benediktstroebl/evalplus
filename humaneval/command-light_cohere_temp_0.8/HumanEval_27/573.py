```python
def flip_case(string):
    return ''.joinnlower(c.lower() if c.isalpha()) else c.isupper()

# prints the original case
# tests
print(flip_case('Hello'))  # Outputs 'H ollehO'
print(flip_case('heLLo'))  # Outputs 'hello'
print(flip_case('cadiao')) # this should pass
```