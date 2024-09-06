```python
def flip_case(string: str) -> str:
    return ''.join_with(str.swap_case(string))

print(flip_case('hello')) # HELLO
print(flip_case('hello World')) # hELLOW World
print(flip_case('isPythonCool'))# iSPOtrCools
```