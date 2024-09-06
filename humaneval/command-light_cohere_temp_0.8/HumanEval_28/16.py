```python
def concatenate(strings: List[str]) -> str:
    return ''.join(strings)

# Test cases
test_concatenate = [
    ['a', 'bc'],
    ['foo', 'bar'],
    ['a', ''],
    ['abcde', 'a']
]

concatenated_results = [
    concatenate(test_concatenate),
    concatenate(test_concatenate) == 'abcde',
    concatenate(test_concatenate) == 'foobarb'
]
print(*concatenated_results)
```