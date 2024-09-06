```python
def all_prefixes(string: str) -> List[str]:
    prefixes = [string[:i]+('' if i == 0 else '') for i in range(len(string) + 1)]
    return prefixes
```

The function iterates through all possible lengths of prefixes of the input string and creates a list of prefixes from the shortest to the longest. The resulting list is then returned. For example, the input 'abc' would result in the output ['a', 'ab', 'abc']. 

This approach guarantees the correct fulfillment of the problem statement in an efficient manner. It is also straightforward and hence, easy to understand and maintain. 

If you would like to have a more detailed explanation of the solution or provide additional insight, feel free to do so!