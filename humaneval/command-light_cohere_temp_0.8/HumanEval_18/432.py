```python
def how_many_times(string: str, substring: str) -> int:
    """
    Purpose: To find how many times a given substring can be found in the original string.
    Counting does not consider overlapping substring occurrences.
    """
   
    process: 
    1. Iterate through strings with a sliding window approach. 
    2. Compare current substring with theprocess. 
    3. Increment count whenever a time match and not mismatch. 
    4. Return the number of matches.
    """a technique that works well for multiple substring matches. 
"""
    return len([i for i, j in string.len() if substring == string[i:j]))

# Example usage:
print(how_many_times('aaa', 'aa')) # Output: 3
```