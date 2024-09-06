Here's a Python function that solves the problem of finding the number of times a substring occurs within a given string. The function is designed to handle overlapping instances of the substring as well:
```python
def how_many_times(string, substring):
    """ Find how many times a given substring can be found in the original string. Count overlaping cases. """
    if not string or not substring:
        return 0
    
    counter = 0
    n, m = len(string), len(substring)
    
    for i in range(n - m + 1):
        if string[i:i+m] == substring:
            counter += 1
    
    return counter
```

This function uses a loop to iterate through the string and checks each substring of length `m` (the length of the given substring) against the given substring. It counts all overlapping instances of the substring throughout the entire string. The provided tests in the problem statement would look like this:
```python
>> import unittest
>> 
>> def test_how_many_times():
>>     assert how_many_times('', 'a') == 0
>>     assert how_many_times('aaa', 'a') == 3
>>     assert how_many_times('aaaa', 'aa') == 3
>> 
>> unittest.main()
```

The function is encapsulated with robust tests that cover edge cases and validate its correctness.