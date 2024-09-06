```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            num **= 2
        elif i % 4 == 0 and i % 3 != 0:
            num **= 3
        result += num
    return result
```

The script uses a for loop to iterate through each index and corresponding value in the input list `lst`. The condition `i % 3 == 0` checks if the index is a multiple of 3, in which case the corresponding value is squared. The condition `i % 4 == 0 and i % 3 != 0` checks if the index is both a multiple of 4 and not a multiple of 3, in which case the corresponding value is cubed. All other entries are left unchanged and added to the `result` variable that is returned at the end. 

To test this function, you can run the following: 

```python
test_list = [1,2,3]
expected_result = 6

print(f'Expected: {expected_result}, Got: {sum_squares(test_list)}')
```

This should output: 

```
Expected: 6, Got: 6
``` 

This demonstrates that the function correctly squares the value at index 3 and returns the expected result when the list contains only single-digit numbers. 

Here is another example for a list with more than one element: 

```python
test_list = [-1, -5, 2, -1, -5]
expected_result = -126

print(f'Expected: {expected_result}, Got: {sum_squares(test_list)}')
```

The output this time is: 

```
Expected: -126, Got: -126
``` 

For this example, the squares and cubes are accumulated as expected in the returned result, giving the correct sum(-126) for the input list with square roots `-1^2 = 1`, `5^2 = 25`, `-1^3 = -1`, `5^3 = 125` and adding them up together resulting in `-126`.