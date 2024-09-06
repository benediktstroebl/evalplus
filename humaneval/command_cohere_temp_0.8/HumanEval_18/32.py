Here's a Python function that solves the problem of finding the number of times a substring occurs in a given string. The function also accounts for overlapping instances of the substring:
```python
def how_many_times(string, substring):
    """ Find how many times a given substring can be found in the original string. Count overlaping cases. """
    count = 0
    n = len(string)
    m = len(substring)
    for i in range(n - m + 1):
        if string[i:i+m] == substring:
            count += 1
    return count
```

This function takes two strings as input: the original string and the substring to search for. It uses a loop to compare the substring to consecutive substrings of the original string, adjusting the starting position to account for overlapping matches. The count variable keeps track of how many times the substring is found. The function returns the total count of occurrences, including overlapping matches. 

Here are some example inputs and expected outputs to demonstrate its functionality:
```python
# Test 1
>>> how_many_times('', 'a')
0
>>> how_many_times('aaa', 'a')
3
>>> how_many_times('aaaa', 'aa')
3
>>> how_many_times('aaa', 'aaa')
1
>>> how_many_times('aa', 'aaa')
0
>>> how_many_times('abcd', 'abcd')
1
```