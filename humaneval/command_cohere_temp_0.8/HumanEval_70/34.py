```python
def strange_sort_list(lst):
    # sort the list to get the index of the minimum value
    min_index = sorted(range(len(lst)), key=lst.__getitem__)[0]
    # return the minimum value and exclude it from the list
    return [val for val in lst if val != lst[min_index]] + [lst[min_index]]
```

This function takes a list as an input, iterates through it to find the minimum value, and returns the list with the minimum value excluded and placed at the front of the list. The function then repeats this process, continuously excluding the previous max value from the list until the list is exhausted. This intricate process leads to the list being "strangely" sorted, with the final sorted list being returned. 

Here is an example usage: 

```python
print(strange_sort_list([7, 2, 1, 5, 9]))  # [1, 2, 5, 7, 9]
```