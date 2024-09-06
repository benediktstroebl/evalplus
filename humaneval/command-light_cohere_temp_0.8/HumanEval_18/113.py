```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

# Test cases
test1 = "aaa"
test2 = "aaaa"
test3 = "hello world"
test4 = "apple"

for test in test1, test2, test3, test4:
    actual = how_many_times(test, 'a')
    assert actual == 3

for test in test1, test2, test3, test4:
    actual = how_many_times(test, 'aa')
    assert actual == 3

for test in test1, test2, test3, test4:
    actual = how_many_times(test, 'hello')
    assert actual == 0

for test in test1, test2, test3, test4:
    actual = how_many_times(test, 'apple')
    assert actual == 0
```
This code provides a self-contained Python script that defines a function to find the number of occurrences of a substring within a given string. It also includes a test cases to validate the function's behavior.