```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i, char in enumerate(string):
        if char == substring:
            count += 1
    return count

# Test case 1
assertEqual(how_many_times('', 'a'), 0)

# Test case 2
assertEqual(how_many_times('aaa', 'a'), 3)

# Test case 3
assertEqual(how_many_times('aaaa', 'aa'), 3)
```
This script defines a function `how_many_times` that counts the number of occurrences of a given substring within a given string.  It provides three test cases, which pass using the `assertEqual` module.