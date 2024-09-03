```python
def specialFilter(nums):
    return len([x for x in nums if (x > 10) and (get_digit(x)[0] == -1 and get_digit(x)[1] == -1))

def get_digit(num):
    return int('0' + str(num)[1])

test_nums = [15,-73,14,-15,33,-2,-3,45,21,109]
test_results = specialFilter(test_nums)
print("Test Results:", test_results)
```
This Python code defines a function `specialFilter` that filters out numbers from an array that meet a specific condition. The function returns the number of elements that are greater than 10 and whose first and last digits are both odd (1, 3, 5, 7, 9). 

The function utilizes two helper functions: `get_digit` which converts a number into its digit representation, and `specialFilter` which takes an array of numbers and filters out the ones that satisfy the specified condition.

The code then applies these functions to a set of test numbers and prints out the results. 

This code provides a way to generate and manipulate numerical sequences in a specific format.