```python
def double_the_difference(lst):
    result = 0
    for num in lst:
        if isinstance(num, int) and num > 0:
            result += num ** 2
    return result
```

The function iterates through each number in the list, and if it's a positive integer, it adds its square to the `result`. This approach ensures that only valid positive integers contribute to the final sum of squares. 

The function returns 0 if the input list is empty, as specified in the problem statement. This behavior is useful to handle potential edge cases and ensure that the function always returns a valid result. 

I hope this Python script will successfully tackle the problem you had in mind! Let me know if you'd like to further refine the solution or tackle different coding problems.