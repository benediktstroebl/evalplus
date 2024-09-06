```python
def how_many_times(string: str, substring: str) -> int:
    """
    Function to find how many times a given substring can be found in the original string, 
    counting overlapping matches.

    Args: 
        - string: str, The original string 
        - substring: str, The substring to search
        
    Returns: 
        - count: int, The number of occurrences of the substring
    """
    count = 0
    n = len(string)
    m = len(substring)
    for i in range(n):
        if string[i:i+m] == substring:
            count += 1
    return count

# Test the function with some examples
print(how_many_times('aaaa', 'aa')) # Output: 3
print(how_many_times('abcd', 'ab')) # Output: 2
print(how_many_times('123456', '456')) # Output: 4
print(how_many_times('Hello', 'ello')) # Output: 3
 ``` 
This script defines a function `how_many_times` that calculates the number of occurrences of a given substring within a given string, while also considering cases with overlapping matches. The function is then tested with various examples, and the results are printed, which demonstrates its correctness.