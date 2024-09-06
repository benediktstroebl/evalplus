```python
def can_arrange(arr):
    prev = arr[0]
    arranged = -1
    for idx, cur in enumerate(arr[1:], start=1):
        if cur > prev:
            return arranged
        elif cur <= prev:
            arranged = idx
        prev = cur
    return arranged
```

The function `can_arrange` iterates through the array, using a variable `arranged` to keep track of the largest index of an element that is not greater than or equal to the previous element. The loop starts from the second element (`arr[1:]`) as the first element has no preceding element to compare to.

During each iteration, the algorithm compares the current element (`cur`) to the previous one (`prev`). If the current element is greater, the algorithm returns the value of `arranged` as the solution. If the current element is eligible to be arranged at the current index (`cur <= prev`), the value of `arranged` is updated to the current index (`idx`).

Finally, if the loop completes without returning, there were no eligible elements, and the algorithm returns -1 as per the problem statement. 

This approach is linear time and uses linear space. It is intuitive and easy to understand, making it suitable for problems like these during coding interviews. 
The solution is capped at O(n) due to the use of only a single loop, making it efficient enough for most interview settings. 

This approach can be optimized further by using a two-pointer approach, swapping elements that are eligible for arrangement. This method reduces the additional space used and improves efficiency slightly. 

It's important to note that this approach assumes the array does not contain any leading zeros, as the first element is used as the baseline for comparison.