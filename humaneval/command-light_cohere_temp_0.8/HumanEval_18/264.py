```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a substring in the original string, 
    while ignoring case and avoiding overlapping occurrences.
    """
   
    string and substring case-insensensitive.
    Returns the time any string containing substring
    """
    return len([i for i,j in zip(string.split(substring,string)) if j == substring])

# Test cases 

print(how_many_times('aaa', 'aa')) # 3
print(how_many_times('ABcd', 'ab'))  # 4
print(how_many_times('Title', 'T'))  # 3
print(how_many_times('s t i l i o u r e', 'hello')) # 3 (till now )
```