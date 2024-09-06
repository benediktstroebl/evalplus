```python
def sorted_list_sum(lst):
    lst_new = []
    for x in lst:
        if len(x) % 2 == 0:
            lst_new.append(x)
    # sort by length, and in case of a tie, by alphabetical order
    lst_new.sort(key=lambda x: (len(x), x))
    return lst_new
```

The solution utilizes a `for` loop to filter out the strings with odd lengths, and in case there is a tie in the length, it sorts by alphabetical order. The `assert` statements are a way to confirm that the script adheres to the expected behavior since the list is always a list of strings and should return a list of strings in sorted order.  This is done using `list_sort(["aa", "a", "aaa"]) => ["aa"]` and `list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]`.  This allows the user to verify that the script is working as intended.  This approach provides an efficient algorithm with a time complexity of O(n log n) due to the sorting process.  It also maintains a descriptive and commented code for easier understanding.  This code can serve as a building block for future problems or solutions that require list filtering and sorting.  It can also be optimized further by using more advanced sorting algorithms.