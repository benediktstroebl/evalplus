```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string, 
    while handling overlapping occurrences.
    """
   
    count = 0
    for i in range(len(string)):
        if string[i] == substring: 
            count += 1
    return count

# Testing the function
>>> how_many_times('aaa', 'a')  # Should return 3
>>> how_many_times('aaaaaaa', 'a')  # Should return 6
```
This code defines a function **`how_many_times`** that finds the occurrences of a given substring within a given string. It returns the how many times the this substring can be found in the original string, while also handling overlapping occurrences.