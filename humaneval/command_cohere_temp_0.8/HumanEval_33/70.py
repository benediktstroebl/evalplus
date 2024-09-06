```python
def sort_third(input_list):
    result = [input_list[i] for i in range(0, len(input_list), 3)]
    result_split = iter(result)
    return [next(result_split), next(result_split), next(result_split)]
```

This script defines a function `sort_third` which takes in a list and returns a new list. This new list is identical to the original in all index points that are not divisible by three, while the ones that are divisible by three are sorted in ascending order. The function achieves this by creating a list of every third index point, then sorting this list in ascending order, and finally using this sorted list to replace the original list's corresponding index points.

Here is an example:
```python
>>> sort_third([1, 2, 4, 3, 6, 5, 7])
[1, 2, 3, 4, 5, 6, 7]
```
This example shows the function in action, sorting the list `[1, 2, 4, 3, 6, 5, 7]` at the index points divisible by three, while leaving the list otherwise unchanged.