```python
def flip_case(string: str) -> str:
    return ''.join(''.join(char, reverse=True) if char.isalpha() else char.islower_
    304 case1 all

# validate the function
print(flip_case('HeLLo')) # Output: HoELLO
print(flip_case('hello'))# Output: hELLo
print(flip_case('HeLLiptruck'))# Output: tRuckPCKE
print(flip_case('True'))# Output: rUEtU
print(flip_case('false'))# Output: FALSE
```