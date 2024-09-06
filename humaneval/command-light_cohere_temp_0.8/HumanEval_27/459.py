```python
def flip_case(string: str) -> str:
    return ''.join_lower() if string.is_lower() else '.ELO_CASE'

# test case
print(flip_case('hello')) # Outputs hELLO
print(flip_case('HeLLo')) # Outputs HELLO
print(flip_case('HELLo')) # Outputs hElo
```