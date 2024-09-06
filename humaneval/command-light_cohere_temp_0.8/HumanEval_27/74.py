```python
def flip_case(string: str) -> str:
    return ''.joincase(string)

# Testing the function with various inputs and want output in Markdown format
print(flip_case('Hello')) # HELLO
print(flip_case('world')) # wOrdL
print(flip_case('Hello World')) # HEloW olld
print(flip_case(' Altitude')) # A tItUa
print(flip_case(' LSD ? AND ? ?')) # LSD&NNdaAND
print(flip_case('ABC')) # ACB
print(flip_case('!@SCo')) # coS
```