```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            result += num ** 2
        elif i % 4 == 0 and i % 3 != 0:
            result += num ** 3
    return result
```

This script defines a function called `sum_squares` taking a list of integers as an input and returning the required sum. The function employs a for loop to iterate through each index of the list and for each index multiple of 3, the function squares the integer, and if the index is a multiple of 4 and not a multiple of 3, the function cubes the integer entry. The final sum is then returned as the function output. 

To ensure the functionality of the script, test the script with example cases provided in the problem statement. Here is an example: 
```python
test = [1,2,3]
assert sum_squares(test) == 6
```

To verify the correctness of the function, the test case should yield a result of 6.