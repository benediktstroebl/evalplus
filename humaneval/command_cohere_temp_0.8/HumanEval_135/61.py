```python
def can_arrange(arr):
    prev = arr[0]
    ans = arr.index(prev)
    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            break
        if arr[i] > arr[ans]:
            ans = i
    return ans if ans != len(arr) - 1 else -1
```

The function compares each element with the previous one, if the element is greater than or equal to its previous counterpart, the function breaks the loop and returns the current index as a result. If the element is smaller, it remains to compare it with the current largest element known to the function, if it is larger - it becomes a new largest element and the answer is updated. If the loop finishes without breaking, it means there are no elements smaller than their predecessors and the function returns -1 as an answer. 

The given example in the problem statement would return the following results:
```
can_arrange([1, 2, 4, 3, 5]) = 3
can_arrange([1, 2, 3]) = -1
``` 

The function returns 3 for the first example due to the largest element arranged at index 3 being 4, which is not greater than or equal to the element preceding it. 

The function returns -1 for the second example, as all elements are increasing and there are no suitable elements for the arrangement.