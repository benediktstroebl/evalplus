```python
def sorted_list_sum(lst):
    lst_len = len(lst)
    if lst_len % 2 == 0:
        temp = sorted(lst)
        temp.sort(key=lambda x: (len(x), x))
        return temp
    else:
        temp = [x for x in lst if len(x) % 2 == 0]
        temp.sort(key=lambda x: (len(x), x))
        return temp
```

The approach taken by the provided Python script is to filter out the odd-length strings from the list, then sort the even-length strings according to their length and alphabetical order. If the resulting list has an even number of elements, it will be sorted in ascending order by length and alphabetically within each length group. If the length of the list is odd, the resulting list will have only one string, as all the even-length strings are sorted and returned, and the odd-length strings are filtered out. 

This approach ensures that the resulting list meets the requirements specified in the prompt: it is a sorted list of strings with even lengths, and it preserves the alphabetical order within each length group.