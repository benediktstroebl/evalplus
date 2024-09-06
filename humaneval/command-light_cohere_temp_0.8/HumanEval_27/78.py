```python
def flip_case(string):
    return ''.join(''.swapcase(string))

print(flip_case('hello')) # Output: 'Hlllo'
print(flip_case('World')) # Output: 'rdl srW'
```