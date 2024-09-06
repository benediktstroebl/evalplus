```python
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    prefixes = [string[0]]
    for i in range(1, len(string)):
        prefixes.append(string[:i])
    return prefixes
```
The function `all_prefixes()` takes a string as input and returns a list of all prefixes in ascending order of length. It starts with a single character as the shortest prefix and then iterates through the string, appending each substring as a prefix until it reaches the full string itself, which is the longest prefix. 
The creator can test this function by calling it with different strings and comparing the output with the desired output.  specifically, the function can be called with the input `abc` and the resulting output verified against the desired output `[('a', 'ab', 'abc')]`.  This process ensures the function operates as expected and aligns with the problem statement. 
This function is also highly efficient given that the resulting list is generated in linear time `O(n)` using a single pass through the input string.  Additionally, the output list has a length proportional to the input string length `n`, resulting in an auxiliary space complexity of O(n).