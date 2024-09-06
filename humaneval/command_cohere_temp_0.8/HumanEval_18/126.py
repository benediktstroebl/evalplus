```python
def how_many_times(string, substring):
    return string.count(substring)
```
```python
def test_how_many_times():
    assert how_many_times("", "a") == 0
    assert how_many_times("aaa", "a") == 3
    assert how_many_times("aaaa", "aa") == 3
```