Here's a Python script that contains a function called `how_many_times` which takes a string `s1` and a substring `s2` and returns the number of times `s2` appears in `s1`, including overlapping instances:
```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    idx = 0
    while idx < len(string) - len(substring) + 1:
        if string[idx:idx + len(substring)] == substring:
            count += 1
            idx += 1
        else:
            idx += 1
            if idx + len(substring) > len(string):
                break
    return count
```

This script defines a function called `how_many_times` that takes two strings as input and returns the number of times the second string appears in the first string, even if overlapping. The function uses a while loop to iterate over the string, checking each substring against the input substring.

To test this function, you can use the following input examples that correspond to the test cases provided in the initial description:
```python
>>> how_many_times('', 'a')
0
>>> how_many_times('aaa', 'a')
3
>>> how_many_times('aaaa', 'aa')
3
```

These examples will help you verify that the function behaves as expected and aligns with the problem definition.