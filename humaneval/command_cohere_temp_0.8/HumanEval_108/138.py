```python
def count_nums(arr):
    output = sum(int(n) for n in arr if sum(map(int, str(n))) > 0)
    return output
```
This function uses a generator expression to iterate over each element in the input list `arr`. It converts each element `n` to an integer using `int(n)`. Then, it calculates the sum of digits using `sum(map(int, str(n)))`. If the sum of digits is greater than 0, it contributes to the count. Finally, it returns the total count of elements meeting this condition. 

Here is the full code including the tests:
```python
def count_nums(arr):
    output = sum(int(n) for n in arr if sum(map(int, str(n))) > 0)
    return output

# Tests
assert count_nums([]) == 0
assert count_nums([-1, 11, -11]) == 1
assert count_nums([1, 1, 2]) == 3
assert count_nums([2, 11, -1, -11, -2]) == 3
```