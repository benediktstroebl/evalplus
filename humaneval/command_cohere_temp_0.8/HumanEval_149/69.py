```python
def sorted_list_sum(lst):
    lst_length = len(lst)
    if lst_length % 2 == 0:
        return lst
    else:
        strings_len_list = []
        for string in lst:
            strings_len_list.append(string)
        strings_len_list.sort()
        temp = []
        for i in range(lst_length // 2):
            temp.append(strings_len_list[i])
        strings_len_list = temp
        return strings_len_list
```

The approach for this solution is:
1. Sort the list alphabetically, and then remove every other element (odd-length elements) until the list is sorted and reduced. 
2. If the list has an even number of elements, return it as it is.
3. If the list has an odd number of elements, omit every second element, sort the remainder, and return it. 

This solution assumes that the list elements are strings and does not consider the possibility of the list containing integers or other types of elements. 

Also, this solution assumes that the list may contain duplicates, and it should remove all odd-length elements from the list until it is sorted. 

This approach results in a time complexity of `O(n log n)` where `n` is the length of the list.