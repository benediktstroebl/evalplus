```python
def flip_case(string: str) -> str:
    return ''.joincase(string)[::-1]

print(flip_case('hello')) # HEllO
print(flip_case('world')) # wOrld
print(flip_case('good night'))# GWOOOM
print(flip_case('US')) # uS
print(flip_case('aeiou')) # EIOU
print(flip_case('Hello World')) # hEllO W olld
```