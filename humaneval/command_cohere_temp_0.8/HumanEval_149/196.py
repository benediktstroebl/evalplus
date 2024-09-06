```python
def sorted_list_sum(lst):
    lst_result = []
    for e in lst:
        if len(e) % 2 == 0:
            lst_result.append(e)
    # sort by len() and alphabetically
    lst_result.sort(key=lambda x: (len(x), x))
    return lst_result
```

The solution uses a simple loop to filter out the odd lengths, and then uses the `sort()` method with a lambda function as the `key` parameter to sort the list first by the length of the words and then by alphabetical order.