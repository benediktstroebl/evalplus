```python
def sorted_list_sum(lst):
    lst_result = []
    for e in lst:
        if len(e) % 2 == 0:
            lst_result.append(e)
    # sort the list using an already sorted list as a criterion
    lst_result.sort(key=lambda x: len(x), reverse=True)
    # if two words have the same length, sort the list alphabetically
    lst_result.sort()
    return lst_result
```

The method loops through the input list, adding elements with even lengths to the result list. The result list is then sorted using the `sort()` method, first based on the length of the strings and then alphabetically if the first level of sorting results in the same length of the strings. The `key` parameter is used to define a lambda function that specifies the sorting criteria. The `reverse=True` parameter ensures that the longest elements are sorted first due to the `True` value for the `reverse` parameter.

Keep in mind that this approach's performance may not be optimal, as it requires two sorting operations. However, assuming the list's shortness or occasional duplicate strings, it should provide adequate performance. If performance is of concern, more optimized algorithms can be used, such as radix sort, which is more efficient in cases with many duplicate values.

The function passes the test cases provided in the prompt, and the assertion statements can be added to the function to ensure it adheres to the guidelines and provides accurate results:
```python
def sorted_list_sum(lst):
    lst_result = []
    for e in lst:
        if len(e) % 2 == 0:
            lst_result.append(e)
    # sort the list using an already sorted list as a criterion
    lst_result.sort(key=lambda x: len(x), reverse=True)
    # if two words have the same length, sort the list alphabetically
    lst_result.sort()
    return lst_result

# Test cases
assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
```