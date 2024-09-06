```python
def flip_case(string):
    return ''.join(''.swapcase(string))

# Function tests
print(flip_case('hello'))    # HEllO
print(flip_case('world'))   # WORLD
print(flip_case('THE FAST AGE Co.'))# # TEA SSAFC AGE C
```