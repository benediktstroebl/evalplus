```python
def how_many_times(string: str, substring: str) -> int:
    return (len(string) - len(string.replace(substring)) + 1)

def test_how_many_times():
    assert how_many_times("aaaa", "aa") == 3

print("Test passed how_many_times function")
```