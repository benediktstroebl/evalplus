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

The code uses a for loop to iterate through each index and corresponding value in the input list `lst`. The conditionals `i % 3 == 0` and `i % 4 == 0 and i % 3 != 0` determine whether to square or cube each number, respectively. Finally, the squared or cubed values are added to the result variable, which is then returned. 

To ensure the function is correct, three test cases are provided:
```python
# test case 1
print(sum_squares([1, 2, 3]))  # 6

# test case 2
print(sum_squares([]))  # 0

# test case 3
print(sum_squares([-1, -5, 2, -1, -5]))  # -126
```

Each test case reflects the examples provided in the problem statement, verifying that the function behaves as expected.