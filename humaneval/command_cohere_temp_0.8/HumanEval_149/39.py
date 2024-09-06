```python
def sorted_list_sum(lst):
    lst = [item for item in lst if len(item) % 2 == 0]
    lst.sort(key=lambda x: (-len(x), x))
    return lst
```
This Python script defines a function **sorted_list_sum** that takes a list of strings as input and returns a sorted list according to the given specifications.

Here's a breakdown of the code:
1. **List Comprehension**: It uses a list comprehension to filter out strings with odd lengths from the input list lst. This step removes all strings with odd lengths from the list.
2. **Sorting**: After filtering, it sorts the list lst based on two characteristics of each string: its length and, in the case of a tie, its alphanumeric order. Using a lambda function, the sorting is done in descending order of length (length of x), and in the case of a tie, it sorts in alphanumeric order (x).
3. **Return**: Finally, the function returns the sorted list of strings.  The result is a list that is sorted first by length, and then by alphanumeric order for items with the same length.