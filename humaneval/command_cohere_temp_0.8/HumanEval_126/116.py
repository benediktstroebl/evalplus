```python
def is_sorted(lst):
    dups = {}
    for x in lst:
        if x in dups:
            dups[x] += 1
        else:
            dups[x] = 1
    for x in dups:
        if dups[x] > 1:
            return False
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
```
This function checks if there's any element in the list that appears more than once, and if so, it returns False, since duplicates violate the criterion of having only single occurrences of each element. If there are no duplicates, it returns True if the list is sorted, otherwise False. This solution has a time complexity of O(n), where n is the length of the input list, and a space complexity of O(n), since it requires the storage of a dictionary to count the duplicates.

Here's a simpler approach using only python's built-in functions:
```python
def is_sorted(lst):
    return lst==sorted(lst)
```
This utilizes python's `sorted()` function to create a sorted version of the input list, and then compares it to the original list through python's equality operator (`==`). If the two lists are equal, it returns True, otherwise, it returns False. This solution has a time complexity of O(n log n), where n is the length of the input list, due to the sorting step, and a space complexity of O(1), as it doesn't require any additional memory beyond the input list. 
This approach, however, does not handle the edge case of lists with elements that appear more than once. It will return false for lists like `[1, 2, 2, 3, 4]` and `[1, 2, 2, 2, 3, 4]`. If you are only interested in the edge cases and assume that general lists will be sorted, this could be an efficient solution.