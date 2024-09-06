```python
def sorted_list_sum(lst):
    lst = [x for x in lst if len(x) % 2 == 0]
    lst.sort(key=lambda x: (-len(x), x))
    return lst
```
This Python script defines a function called `sorted_list_sum` that takes a list of strings as input. It filters out any strings with odd lengths using a list comprehension, ensuring that the list only contains strings with even lengths. Then, it sorts the list using a sorting key that prioritizes negative string lengths, ensuring that the list is ordered by decreasing string lengths. If two strings have the same length, the alphabetical order is used as a secondary sorting criteria, ensuring the list is sorted alphabetically in case of ties. The function returns the final sorted list of strings.

Here's an example usage of the function:
```python
print(sorted_list_sum(["aa", "a", "aaa", "ab", "c", "aaa", "cd"]))
```

The function can be tested with the following Python code:
```python
def test_sorted_list_sum():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
    assert sorted_list_sum(["aa", "ab", "ac", "a", "ba", "b", "ca", "c"]) == ["aa", "ab", "ac", "ba", "bb", "bc", "ca", "c"]
    assert sorted_list_sum(["zz", "zzz", "zzzz"]) == ["zz", "zzz", "zzzz"]
```

This test code validates the behavior of the `sorted_list_sum` function with three test cases, asserting that the resulting lists are correctly sorted as specified by the problem statement.