```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    n = len(string)

    for i in range(n):
        if string[i] == substring:
            count += 1

    return count

# Test suite below
def test_how_many_times():
    assert how_many_times('abcde', 'a') == 3
    assert how_many_times('abcbaa', 'a') == 6
    assert how_many_times('aaaa', 'a') == 3
    assert how_many_times('abcdef', 'def') == 1
    assert how_many_times('abcba', 'ab') == 2
    assert how_many_times('abcba', 'ab') == 3
    assert how_many_times('abcba', 'Xxx') == 0
```
This Python script defines a function `how_many_times` that counts how many times a given substring can be found in a string. It then provides a test suite with several tests to ensure the correctness of the function.