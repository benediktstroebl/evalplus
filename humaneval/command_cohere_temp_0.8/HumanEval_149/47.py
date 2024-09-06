```python
def sorted_list_sum(lst):
    lst = [e for e in lst if len(e) % 2 == 0]
    # Sorting the list in ascending order
    # Based on the length and alphabetically
    lst.sort(key=lambda x: (len(x), x))
    return lst
```

This script sorts the list based on the length of each element in the list and in the case of a tie, it sorts the list alphabetically. The function returns the list in an ascending order.

The function `sorted_list_sum()` takes the list of strings as a parameter and returns a list of strings sorted in the specified manner. It deletes all strings with odd lengths using a list comprehension, which filters out only even lengths. Then it sorts the list based on the length of each string first and uses the second element as a tie breaker.

Note: The code uses Python 3 syntax and conventions, including the `def` keyword for function definition and list comprehension for filtering out odd-length strings.  In Python 3, `print` is a reserved word, so the code uses the `print()` function for displaying test results.  If you plan to run this code in Python 2, you may need to rewrite the syntax to comply with Python 2 conventions.  Also, this code assumes that the list elements are strings; if you have a list of numbers, you may need to modify the `key` parameter in the `sort()` function to handle numerical values appropriately.  Finally, the code assumes that the list may contain duplicates; if this is not the case, the list comprehension can be simplified to `filter(lambda x: len(x) % 2 == 0, lst)`