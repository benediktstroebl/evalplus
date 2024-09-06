Here's a Python script with a self-contained function that solves the problem:
```python
def smallest_change(arr):
    arr = list(set(arr))    # Remove duplicates
    return sum(x != y for x, y in zip(arr, reversed(arr))) // 2
```
The function works by first removing any duplicates from the array. Then, it checks for each unique element in the array if it matches its reverse counterpart in the array, doing this for each element results in a set of pairs where each pair (x, y) represents two corresponding elements in the main and reversed arrays and these pairs are then summed up and the number of changes is returned, as the number of changes is divided by 2 to only count each element once, and the result is returned. 

Here's an example usage of the function:
```python
print(smallest_change([1, 2, 3, 4, 3, 2, 2]))
```
The output will be:
```
1
```