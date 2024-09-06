```python
def sorted_list_sum(lst):
    lst = [x for x in lst if len(x) % 2 == 0]
    # Sorting the list in ascending order
    lst.sort(key=lambda x: (len(x), x))
    return lst
```
The problem asks for a function that takes a list of strings, deletes the strings with odd lengths, and returns the remaining strings in a sorted order. This is passed as a parameter in a list of strings with different lengths, and duplicates may be present. The order should be ascending based on the length of each word, and in the case of the same length, it should be in alphabetical order. The function returns a list of strings in the sorted order as described. 

The function `sorted_list_sum()` does not return the sum of the list, but rather processes a list of strings, eliminating odd-length strings, and returns the remaining strings in sorted order. This is accomplished by using a list comprehension to filter out the odd-length strings, and then sorting the list using a lambda function as the key. The lambda function sends each string to a tuple with the first element being the length of the string and the second element being the string itself. This guarantees that the list will be sorted first by string length and, for strings of the same length, will be sorted alphabetically. 

This code does not include any testing capabilities, but it does provide a solution to the problem statement and is testable with the provided tests.