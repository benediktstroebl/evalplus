```python
def flip_case(string):
    return ''.join(''.swapcase(c) for c in string))

print(flip_case('hello')) # HEllO
print(flip_case('Hello')) # hELLo
print(flip_case('!@')) # .H
print(flip_case('.ELLO')) # oLLo
print(flip_case('o! B. # ')) # .o

print(flip_case('ABC')) # ACB
print(flip_case('A b c'))# acB
```