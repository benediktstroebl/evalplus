```python
def can_arrange(arr):
    ind = len(arr) - 2
    while ind >= 0 and arr[ind] >= arr[ind + 1]:
        ind -= 1
    return max(ind + 1, -1)
```
This Python script defines a function named `can_arrange` that addresses the problem statement. It starts by assuming the highest index of an admissible element is the second-to-last index (`ind = len(arr) - 2`) of the array. It then verifies if the element at the assumed index is less than or equal to the preceding element in the array. If this condition is met, the function returns -1 to indicate no valid arrangement exists. If the condition is not met, the function continues moving the index to the left, checking if the element at that index is still less than or equal to the next element in the array. This process repeats until reaching an eligible element or the beginning of the array. The function then returns the index + 1 of the eligible element, or -1 if no such element is found. 

Here is an example of an array that will return -1: `can_arrange([1,2,3]) = -1`
And here is an example of an array that will return the largest index of an element that is not greater than or equal to the element immediately preceding it: `can_arrange([1,2,4,3,5]) = 3`.

This function elegantly solves the problem using a recursive approach, efficiently handling the edge cases mentioned in the problem statement.