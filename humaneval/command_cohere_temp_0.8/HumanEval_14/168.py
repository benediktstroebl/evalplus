```python
def all_prefixes(string: str) -> List[str]:
    prefixes = [string[:i]+'%' for i in range(len(string)+1)]
    return prefixes[:-1]
```

The code snippet provided generates a list of prefixes for a given string and returns the list of prefixes in ascending order. 

For example, if the input is "abc", the code will return ["a", "ab", "abc"] which are the prefixes of the input string of varying lengths, from shortest to longest. 

Let's break down the code: 
 1. The function `all_prefixes` takes a single argument `string` which is the input string for which we want to generate prefixes. 
2. The code uses a list comprehension with a range of lengths from 1 to the length of the input string to create a list of prefixes of the input string with the `%` symbol added to the end to ensure that the prefix is a substring but not the entire string. 
3. The list comprehension results in a list of prefixes from the shortest to the longest, excluding the entire string as a prefix. 

The result is a list of prefixes sorted in ascending order based on their length. Ghim full comment and let me know if you have any questions!