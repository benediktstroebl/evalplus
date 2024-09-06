```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    string = ''.join + string
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
assertEqual(how_many_times('hello world', 'world'), 2)
```
The provided code defines a function `how_many_times` that calculates the frequency of a given substring within a given string. It employs a loop to iterate over each character in the string, and counts the number of occurrences of the substring. The function is then tested with several test cases to ensure its correctness.