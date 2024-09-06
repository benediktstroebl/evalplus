```python
def sorted_list_sum(lst):
    lst_new = []
    for i in lst:
        if len(i) % 2 == 0:
            lst_new.append(i)
    lst_new.sort()
    for i in range(len(lst_new)-1):
        if lst_new[i] == lst_new[i+1]:
            lst_new[i+1] = lst_new[i] + lst_new[i+1]
    return lst_new
```
This code block implements the `sorted_list_sum` function specified in the problem statement. It takes as input a list of strings, `lst`, and returns a new list where elements are stripped down to their odd index characters and sorted in ascending order.

The algorithm can be broken down into the following steps:
1. Iterate through each element in the input list:
   - If the length of the current element is divisible by 2, it means it has an even number of characters. Add it to a new list, `lst_new`.
2. Sort the elements in `lst_new` in ascending order.
3. Check if any adjacent elements in `lst_new` are duplicates:
   - If so, concatenate the duplicate elements horizontally to ensure only one occurrence in the final list.
4. Return the cleaned and sorted `lst_new`.

This algorithm efficiently cleans and sorts the list as specified in the statement.