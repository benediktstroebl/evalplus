Here's a Python function that solves the problem you've described, with code examples and a demonstration of how the function behaves for different inputs:
```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    substring_length = len(substring)
    string_length = len(string)
    
    for i in range(string_length - substring_length + 1):
        if string[i:i+substring_length] == substring:
            count += 1
    
    return count

# Tests
assert how_many_times('', 'a') == 0
assert how_many_times('aaa', 'a') == 3
assert how_many_times('aaaa', 'aa') == 3
assert how_many_times('abaabaa', 'aa') == 3
```

This function, `how_many_times`, accepts a string `string` and a substring `substring` as inputs. It counts the number of times the `substring` appears in the `string`, even if the instances overlap. The provided tests demonstrate the behavior of the function for different inputs.