```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

# Test case 1
assertEqual(how_many_times('', 'a'), 0)

# Test case 2
assertEqual(how_many_times('aaa', 'a'), 3)

# Test case 3
assertEqual(how_many_times('aaaa', 'aa'), 3)

# Test case 4
assertEqual(how_many_times('abcde', 'abc'), 2)

# Test case 5
assertEqual(how_many_times('defgats', 'ats'), 2)
```
This script defines a function `how_many_times` that counts the number of occurrences of a given substring in a given string. It uses a easy and efficient approach with a loop to achieve this. The test cases validate the expected behavior of the function with various input strings and substring.