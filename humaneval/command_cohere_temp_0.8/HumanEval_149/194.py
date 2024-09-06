```python
def sorted_list_sum(lst):
    lst = [item for item in lst if len(item) % 2 == 0]
    lst.sort(key=lambda x: (-len(x), x))
    return lst
```
This Python script defines a function called `sorted_list_sum` that takes a list of strings as input. It filters out any strings with odd lengths using a list comprehension, ensuring that the list contains only strings with even lengths. Then, it sorts the list using a lambda function with two key parameters: the first is the negative length of the string, which ensures that longer strings come first. If two strings have the same length, the second key parameter, the string itself, is used for alphabetical sorting. The resulting sorted list is returned.

Here's an example usage of the function from the prompt:
```python
assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
```
This example test case verifies the function's behavior against the provided problem statement, confirming that the function correctly filters out odd-length strings, sorts the list by length, and returns the expected result.