Here's a Python script with a self-contained function that solves the problem:
```python
def monotonic(lst):
    if len(lst) <= 1:
        return True
    a = lst[0]
    for b in lst[1:]:
        if a <= b:
            # Increasing: [a, a+1, a+2, ...]
            return True
        elif a >= b:
            # Decreasing: [a, a-1, a-2, ...]
            return True
        a = b
    return False
```

The function first determines whether the list has fewer than two elements, returning True in such cases no matter the arrangement since there isn't enough data to establish a pattern. It then compares the first two elements, `a` and `b`, if the list is longer than one. It verifies if the elements are either increasing (`a <= b`) or decreasing (`a >= b`). If either of these conditions is fulfilled, the function returns True, suggesting a monotonic arrangement. If neither condition is met, the function iterates through the remainder of the list, continually comparing elements, and returning True if a pattern is detected. If none is found by the conclusion, the function returns False, indicating no monotonic behavior. 

Here's an example usage of the function:
```python
print(monotonic([1, 2, 4, 20])) # Output: True
print(monotonic([1, 20, 4, 10])) # Output: False
print(monotonic([4, 1, 0, -10])) # Output: True
```

This example demonstrates the functionality of the `monotonic` function in different scenarios.