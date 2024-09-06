```python
def sorted_list_sum(lst):
    lst = [str(ele) for ele in lst if len(ele) % 2 == 0]
    return sorted(lst, key=lambda x: (len(x), x))
```
The problem asks for a function that takes a list of strings, deletes the strings with odd lengths, and returns the remaining strings in a sorted order. This is achieved through the following steps:
1. Use a list comprehension to filter out the strings with odd lengths present in the list. This guarantees that all elements in the list are strings and have even lengths.
2. Use the `sorted` function to sort the list of strings in ascending order. The sorting key is a lambda function that takes each string and extracts its length and value. In case of a tie, it sorts the elements alphabetically. 

This approach efficiently solves the problem and produces the required output.