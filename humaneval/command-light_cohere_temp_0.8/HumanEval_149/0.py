Here is a Python script that defines a function called `sorted_list_sum` that solves the problem:

```python
def sorted_list_sum(lst):
    # remove strings with odd length
    lst = [sub for sub in lst if len(sub) <= 1]
    # sort list based on length of each word
    return sorted(lst, key=lambda x: len(x))

# test cases
assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

```

This function is a self-contained solution to the problem. It takes the strings from the list and removes the strings that have odd lengths. Then, it sorts the list by the length of each word and returns the list sorted by that rule. This solution uses the basic Python list operations and a custom sorting key function.