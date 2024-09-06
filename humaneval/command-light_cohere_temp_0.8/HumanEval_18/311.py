Here's a self-contained Python script that solves the problem of counting the number of occurrences of a given substring within a given string:
```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for char in substring:
        if char in string:
            count += 1
    return count

# Unit tests
test_how_many_times = {
    "test 1" :lambda: how_many_times('aaaa', 'aa'),
    "test 2" :lambda: how_many_times('abcde', 'abcde'),
    "test 3" :lambda: how_many_times('abcba', 'abcba'),
    "test 4" :lambda: how_many_times('abcba', 'ab'),
    "test 5" :lambda: how_many_times('abc', 'ab'),
    "test 6" :lambda: how_many_times('abc', 'ABC'),
    "test 7" :lambda: how_many_times('', 'a'),
    "test 8" :lambda: how_many_times('aaa', 'aaa'),
    "test 9" :lambda: how_many_times('abcde', 'cd'),
    "test 10" :lambda: how_many_times('abcba', 'ab'),
    }

for test, expect in test_how_many_times.items():
    assert expect == how_many_times(*test)
```
This script defines a function `how_many_times` that takes a string and a substring as input and returns the number of occurrences of the substring within the string. It is also includes a set of unit tests to verify the correctness of the function.