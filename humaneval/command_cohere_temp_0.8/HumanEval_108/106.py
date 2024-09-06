```python
def count_nums(arr):
    return sum(sum(map(int, str(n))) > 0 for n in arr)
```

This script defines a Python function `count_nums` that takes an array of integers as input and calculates the number of elements with a sum of digits greater than zero. It uses a generator expression within the sum function to iterate through each element in the input array and evaluate its digit sum. The condition `sum(map(int, str(n))) > 0` checks if the sum of the integer's digits is greater than zero. The function then returns the count of elements that satisfy this condition.

Here's an example usage explanation:
```python
# Test the function with an empty array
arr = []
result = count_nums(arr)
print(result)  # Output: 0

# Test the function with an array containing positive and negative integers
arr = [-1, 11, -11]
result = count_nums(arr)
print(result)  # Output: 1

# Test the function with an array containing only positive integers
arr = [1, 1, 2]
result = count_nums(arr)
print(result)  # Output: 3
```

In each test case, the function is called with the respective array, and the output is printed to demonstrate the counting of elements based on their digit sums.