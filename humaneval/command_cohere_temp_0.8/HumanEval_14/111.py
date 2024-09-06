```python
def all_prefixes(string: str) -> List[str]:
    prefixes = [string[:i] for i in range(len(string) + 1)]
    return prefixes
```

This function defines a list of prefixes by using a list comprehension that generates all prefixes from the smallest to the largest. The function iterates through the length of the given string and creates a substring starting from position 0 up to the current position in an anti-clockwise direction. The resulting list of prefixes is then returned. 

To follow the type hint of the function, the list is typed as a list of strings to match the input of the function as a string. 

This approach ensures that every possible prefix of the input string is captured, including the empty prefix, making it a valid solution to the problem.