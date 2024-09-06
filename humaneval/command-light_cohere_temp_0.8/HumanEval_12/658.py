Here is a Python script that contains a self-contained function that solves the problem of finding the longest string in a list of strings:
```python
def longest(strings: List[str]) -> Optional[str]:
    """
    Returns the longest string in the list.
    Parameters: List[str]
    Returns: The longest string in the list.
    Returns None if the string list is empty.
    """
   
    longest([]) --> None
    longest(['a', 'b', 'c']) --> 'a'
    longest(['aa', 'bb', 'ccc']) --> 'ccc'
    longest(['abcd', 'abcdab', 'abcd']) --> 'abcdab'
    longest(['aa', 'bb', 'ccc'])['ccc']
    longest(['aa', 'bb', 'ccc', 'aaa'])['aaa']
    longest(['abcde', 'ab', 'ace'])['ace']
    longest(['abcde', 'ab', 'ace', 'abcd'])['abcd']
    """
    if not strings:
        return None
    max_length = 0
    for string in strings:
        if len(string) > max_length:
            max_length = len(string)
    return strings[max_length]
```
This function takes a list of strings as input and returns the longest string in the list. It handles empty lists gracefully and provides clear test cases to demonstrate its behavior.