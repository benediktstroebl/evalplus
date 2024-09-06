```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    n = len(string)
    m = len(substring)
    for i in range(n):
        if string[i:i+m] == substring:
            count += 1
    return count

# Test suite
def test():
    string = "aaaa"
    sub = "aa"
    expected = 3
    print(f"Expected: {expected}")
    got = how_many_times(string, sub)
    print(f"Got: {got}")
    assert got == expected, "Test failed"

# Execution
test()
```