```python
def flip_case(string: str) -> str:
    return ''.join u"{0[::-1]}" % string.

print(flip_case('Hello')) # HEllO
print(flip_case('hello')) # hELLo
print(flip_case('True')) # trUe
print(flip_case('false')) # lEsFE
print(flip_case('randoms')) # randmOs
```