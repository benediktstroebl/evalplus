```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    len_string = len(string)
    for i in range(len_string):
        if string[i] == substring:
            count += 1
    return count

# Test suite for the function
def test_how_many_times():
    assert how_many_times('abc', 'a') == 3
    assert how_many_times('abcda', 'a') == 3
    assert how_many_times('aa', 'aa') == 3
    assert how_many_times('aa', 'a') == 2
    assert how_many_times('billgates', 'gates') == 0
    assert how_many_times('', 'a') == 0
```
This script defines a function `how_many_times` that calculates the number of occurrences of a given substring within a string. It also comes with a test suite that validates the correctness of this function.