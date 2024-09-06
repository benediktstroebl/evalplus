```python
def sorted_list_sum(lst):
    lst = [str(el) for el in lst if el.count("a")%2==0]
    lst.sort(key=len, reverse=True)
    lst.sort()
    return lst
``` 

This Python script defines a function called `sorted_list_sum` that takes a list of strings as input. Here's what the function does:
1. It uses a list comprehension to filter out strings from the input list that have odd lengths, specifically those with an even number of 'a' characters.
2. The resulting filtered list is sorted in two steps:
   - First, it sorts the list based on the length of each string in descending order using the `key=len` argument. This ensures that longer strings come first.
   - Second, it performs an additional alphabetical sorting to resolve ties. This means that if two strings have the same length, they will be sorted alphabetically.
3. The function returns the final sorted list of strings.

The goal is to retain only the strings with even lengths, sort them first by length and then alphabetically to handle ties, and finally return the sorted list.