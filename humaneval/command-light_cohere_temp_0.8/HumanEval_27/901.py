```python
def flip_case(string: str) -> str:
    return ''.joincase(string.make_lower()) if not string else string.get_upper()


# Example
test_flip_case = flip_case.assertEqual_test_string = 'hello'
print(test_flip_case) # Output: HELLO
```