```python
def how_many_times(string: str, substring: str) -> int:
    return sum(1 for char in substring if char in string)

# Test cases
tests = {
    'string': ['a', 'aa', 'aaaa'],
    'substring': 'a'
}

assert how_many_times('aaa', 'a') == 3
assert how_many_times('aaaa', 'aa') == 3
assert how_many_times('abcde', 'cde') == 4

# Main function call
string = 'aaaaaaa'
substring = 'aaaa'
result = how_many_times(string, substring)

print("Result:", result)
```