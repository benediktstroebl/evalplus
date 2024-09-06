```python
def flip_case(string: str) -> str:
    return ''.join("".swapcase(string))

#Tests
test_flip_case = FlipCase()
test_flip_case.test_flip_case("hello"))
# ... (remaining tests)
```
This function flips the case of all characters in a given string.