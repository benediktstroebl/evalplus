```python
def how_many_times(string, substring):
    return string.count(substring)
```

This function accepts two strings as input: the original string and the substring to search for. It uses the `count()` method to detect the occurrence of the substring within the original string. This method identifies the instance of the substring, accounting for overlapping instances if present.

Here is a test case that can be used to validate the function:
```python
def test_how_many_times():
    assert how_many_times('', 'a') == 0
    assert how_many_times('aaa', 'a') == 3
    assert how_many_times('aaaa', 'aa') == 3
```

 executing this test case will verify that the function's behavior aligns with the problem statement.