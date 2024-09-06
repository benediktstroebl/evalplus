```python
def pairs_sum_to_zero(l):
    # iterate through all pairs
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] + l[j] == 0:
                return True
    return False
```

This function uses two nested loops to iterate through all possible pairs of elements in the list and checks if their sum is equal to zero. It returns True if any such pair is found and False otherwise.

The function is self-contained and can be used in a Python script to solve the problem, as it doesn't rely on external variables or functions. 

It also passes the tests provided in the prompt, as shown in the example below:
```python
tested_list = [1, 3, 5, 0]
print(pairs_sum_to_zero(tested_list))  # Expected output: False

tested_list = [1, 3, -2, 1]
print(pairs_sum_to_zero(tested_list))  # Expected output: False

tested_list = [1, 2, 3, 7]
print(pairs_sum_to_zero(tested_list))  # Expected output: False

tested_list = [2, 4, -5, 3, 5, 7]
print(pairs_sum_to_zero(tested_list))  # Expected output: True

tested_list = [1]
print(pairs_sum_to_zero(tested_list))  # Expected output: False
``` 
This code snippet demonstrates the usage of the 'pairs_sum_to_zero' function with different input lists, and the output matches the expected results provided in the original problem description.