Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This script defines a function called `incr_list` that takes a list `l` as input and returns a new list where each element is incremented by 1. It uses a list comprehension to iterate over each element in the input list and adds 1 to it, effectively incrementing it. The function includes no additional dependencies or external code, making it self-contained.

To test this function, you can run the following code:
```python
test1 = [1, 2, 3]
test2 = [5, 3, 5, 2, 3, 3, 9, 0, 123]

print("Test 1:", incr_list(test1))
print("Test 2:", incr_list(test2))
```

Expected output:
```
Test 1: [2, 3, 4]
Test 2: [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

This demonstrates that the `incr_list` function correctly increments each element in the list by 1, producing the desired result. Note that the function includes no external dependencies, making it self-contained and easier to maintain and integrate into various codebases.