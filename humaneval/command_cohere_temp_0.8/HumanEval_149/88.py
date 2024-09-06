```python
def sorted_list_sum(lst):
    lst = [e for e in lst if len(e) % 2 == 0]
    # sort by len() and alphabetically
    lst.sort(key=lambda x: (len(x), x))
    return lst
```
This Python script defines a function called `sorted_list_sum` that takes a list of strings as input. Here's what the function does:
1. It filters out any strings from the input list that have odd lengths using a list comprehension. These strings are not considered for further processing and are discarded.
2. The function then sorts the list of strings that remain after the filtering process. The sorting is performed in two steps:
- First, it sorts the strings based on their lengths, so that shorter strings come before longer ones.
- If two or more strings have the same length, they are further sorted alphabetically in ascending order.
3. Finally, the function returns the sorted list of strings that meet the criteria (even-length words and alphabetical order for equal-length words).

This approach ensures that the list is sorted by word length and alphabetically within groups of equal-length words, as specified in the problem statement.