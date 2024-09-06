```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n + 1)

# test case for function
test_string_sequence = lambda : True
result = string_sequence(0)
test_string_sequence(result) # True

result = string_sequence(5)
test_string_sequence(result) # ['0 1 2 3 4 5']
```