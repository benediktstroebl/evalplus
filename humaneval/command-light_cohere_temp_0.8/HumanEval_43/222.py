Here's a self-contained Python script with a function that solves the problem of checking whether all elements in a list sum up to zero:
```python
def pairs_sum_to_zero(l):
    return any([x for x in l if x <= 0])

#Test cases 

#Test 1: Lists the sum of positive numbers
[1, 3, 5, 0] => False

#Test 2: Lists the sum of negative numbers
[1, 3, -2, 1] => False

#Test 3: Lists the sum of all numbers (including zero)
[1, 2, 3, 7] => False

#Test 4: Empty list
[] => False

#Test 5: Lists the sum of all numbers (including zero) in a list of positive numbers
[2, 4, 6, 8] => True

#Test 6: Lists the sum of all numbers (including zero) in a list of negative numbers
[-2, -4, -6, -8] => True

#Test 7: Lists the sum of all numbers (including zero) in a mix list
[1, 2, 3, 7] [] => False
```
The script includes a variety of test cases to ensure the function `pairs_sum_to_zero` correctly identifies lists where the sum of all elements equals zero.