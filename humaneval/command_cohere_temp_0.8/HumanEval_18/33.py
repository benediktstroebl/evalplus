Here's a Python script with a self-contained function that solves the problem you've described, including a markdown code block showing the complete script:
```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    count = 0
    for i in range(len(string)):
        for j in range(i, len(string)):
            if string[i:j+1] == substring:
                count += 1
    return count
```
This script defines a function `how_many_times(string, substring)` that takes a string `string` and a substring `substring` as input, and returns the number of times the substring occurs within the string, even if the substring occurs multiple times in consecutive fashion. 

The function uses two nested loops to compare the substring to each possible consecutive window of the same size in the string. The count is incremented each time a match is found. The total count is returned at the end.

The function is called with test cases in the docstring, which are meant to illustrate how the function behaves. You can use these test cases to verify the correct operation of your function.