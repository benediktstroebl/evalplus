```python
def all_prefixes(string: str) -> List[str]:
    prefixes = [string[:i]+('' if i==0 else ' ') for i in range(len(string)+1)]
    return prefixes
```

The function generates all prefixes with the length of the input string and incrementally decreases the length by 1 in each iteration. The `range(len(string)+1)` is used to determine the number of iterations which is len(input string) + 1, representing the number of characters in the input string and the 0-length string (i.e. ''). A list of prefixes is created by iteratively taking the substring of length i (inclusive) for each i in the range and concatenating it with an empty string (to create space between words) or a space character (' '), depending on whether the i is 0 (which indicates the prefix should be a single-character string).  It is important to note, that the returned list is sorted from the shortest to the longest prefix.