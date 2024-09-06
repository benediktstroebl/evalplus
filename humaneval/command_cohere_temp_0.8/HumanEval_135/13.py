```python
def can_arrange(arr):
    ind = len(arr) - 2
    while ind >= 0 and arr[ind] >= arr[ind + 1]:
        ind -= 1
    return max(ind + 1, -1)
```
This Python script defines a function named `can_arrange` that addresses the problem statement. It starts by assuming the last element is the one that should be checked and initializes `ind` to `len(arr) - 2`. It then checks if this assumption is incorrect, iterating through the array using a `while` loop with an initial condition of `ind >= 0` and the loop condition of `arr[ind] >= arr[ind + 1]`. In each iteration, it moves the index forward, checking if the current element is greater than or equal to the next one. When an element that doesn't satisfy this condition is found, the loop ends, and the index is adjusted to check the previous element, if such a previous element exists. The function then returns the largest index of an element that isn't greater than or equal to the preceding one, accounting for the possibility that no such element exists, in which case it returns -1.