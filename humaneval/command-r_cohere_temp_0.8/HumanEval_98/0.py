```python
def count_upper(s):
    """
    Count uppercase vowels in even indices.
    
    Args:
        s (str): Input string.
        
    Returns:
        int: Number of uppercase vowels in even indices.
    """
    vowels = "AEIOUaeiou"
    count = 0
    for idx in range(len(s)):
        if s[idx] in vowels and idx % 2 == 0:
            count += 1
    return count
```