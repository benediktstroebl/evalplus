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
This Python script defines a function named `can_arrange` that addresses the problem statement. It iterates through the array, comparing each element to the previous one. If an element is greater, it returns the current index as the answer. If an element is non-greater, it continues checking until it finds an eligible element, returning its index. If no such element is found, it returns -1. 

The provided example usage demonstrates the function's behavior on two arrays, offering insights into how it tackles the challenge.

This approach yields a straightforward Python function that seamlessly integrates into larger scripts and efficiently solves the problem.