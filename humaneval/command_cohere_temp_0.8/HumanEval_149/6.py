```python
def sorted_list_sum(lst):
    lst = [e for e in lst if len(e) % 2 == 0]
    lst.sort(key=lambda x: (-len(x), x))
    return lst
```
This Python script defines a function called `sorted_list_sum` that takes a list of strings as input. It filters out any strings with odd lengths using a list comprehension, ensuring that the list only contains strings with even lengths. Then, it sorts the list using a lambda function with two key parameters: the first one reverses the sorting order based on the length of each string, and the second key sorts the strings alphabetically if the first key is the same. This ensures that the resulting list is sorted by string length in descending order and alphabetically for strings with the same length. The function returns the final sorted list of strings.

Here's an example usage of the function:
```python
print(sorted_list_sum(["aa", "a", "aaa", "ab", "c", "aaa", "cd"]))
```

The function can be tested with the following assert statements:
```python
assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
assert sorted_list_sum(["xx", "xx", "xy", "xz", "yy", "yy", "yz"]) == ["xy", "xx", "xz", "yy", "yz"]
```

The function should handle any list of strings, including lists with duplicates and odd-length strings, and return the sorted list based on the given sorting rules.