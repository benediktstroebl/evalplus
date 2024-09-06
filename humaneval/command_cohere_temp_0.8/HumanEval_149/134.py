```python
def sorted_list_sum(lst):
    lst_result = []
    for e in lst:
        if len(e) % 2 == 0:
            lst_result.append(e)
    # sort the list alphabetically and by the length of words, ascendingly
    lst_result.sort(key=lambda x: (len(x), x))
    return lst_result
```

The method `sorted` is used to sort the list, the argument `key=lambda x: (len(x), x)` states that the sorting is done by the length of the words in the list and, in case of a tie, it sorts the list alphabetically. 

A few test cases are provided to test the function with different input lists. You can add more test cases to ensure the function works correctly for any possible input. Here is how you could do it:
```python
assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
assert sorted_list_sum(["ab", "cd", "aaa", "a"]) == ["a", "aa", "ab", "cd"]
```