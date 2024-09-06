```python
def how_many_times(string: str, substring: str) -> int:
    return len(string.find(substring))

#unit tests
test_ Cases = [
    ("a", "a"),
    ("aaaaaa", "aa"),
    ("aaaa", ""),
    ("", ""),
    ("a", "b"),
    ("aaa", "ab"),
    ("aa", "ab"),
    ("aaa", "aaa")
]
for case in test_Cases:
    actual = how_many_times(*case)
    expected = len(case)
    print(f"Case: actual, expected)
    if actual != expected:
        print("fail", actual, expected)
```