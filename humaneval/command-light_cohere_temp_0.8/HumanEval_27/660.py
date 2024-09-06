```python
def flip_case(string: str) -> str:
    return ''.joincase(string)[::-1]

print(flip_case('Hello'))
 #HLELo
print(flip_case('world'))
 #Wroolld
print(flip_case('good morning'))
 #GoOD npdiagno
print(flip_case('First'))
 # fiST
print(flip_case('test'))
 #STe
```