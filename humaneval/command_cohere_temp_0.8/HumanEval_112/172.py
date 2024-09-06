```python
def reverse_delete(s, c):
    delete = [char for char in c]
    reverse = s[::-1]
    pm = 0
    for i in range(len(s)):
        if s[i] in delete and reverse[pm] != s[i]:
            pm += 1
    temp = s[pm::]
    if temp == temp[::-1]:
        return (temp, True)
    else:
        return (temp, False)
```

The solution utilizes the fact that the string to be checked for being a palindrome, after deletion of characters from `c`, is always reversed and palindrome characteristics are checked simultaneously for both the original and reversed strings. The function `reverse_delete()` returns a tuple containing the result string and a boolean indicating whether it's a palindrome (True) or not (False). 

This solution has a time complexity of O(n) where n is the length of the string `s` since two passes through the string are made and the maximum number of operations at any point is O(n).

This solution should be placed in a Python file with appropriate testing code to validate its correctness and robustness. For example, you could include tests like:
```python
def test_reverse_delete():
    assert reverse_delete("abcdef", "b") == ('acdef', False)
    assert reverse_delete("abcde", "ae") == ('bcd', False)
    assert reverse_delete("abcdedcba", "ab") == ('cdedc', True)
    assert reverse_delete("a", "a") == ('', True)
    assert reverse_delete("aaaaaaa", "aa") == ('a', True)
    assert reverse_delete("abcdef", "cd") == ('aef', False)
``` 
This way, you can ensure the function performs as expected across different scenarios.