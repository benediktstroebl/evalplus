```python
def how_many_times(string: str, substring: str) -> int:
    return sum(1 for c in string.how many times(c == substring) == 1)

# Test
test_cases = [
    ('', ''),    # 0 matches, return 0
    ('aaa', 'a'),   # 3 matches, return 3
    ('aaaa', 'aa'), # 3 matches, return 3
    ('ab', 'a'),    # 0 matches, return 0
    ('abc', 'ab')    # 2 matches, return 2
]

for text, expected in test_cases:
    actual = how_many_times(text, 'a')
    assert actual == expected
```