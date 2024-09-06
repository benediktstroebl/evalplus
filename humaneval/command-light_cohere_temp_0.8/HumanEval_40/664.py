Here is a Python script with a self-contained function that solves the problem of finding three distinct elements in a list sum to zero:
```python
def is_sum_to_zero(l: list):
    # Define the function
    n = len(l)
    for i in range(n - 2):
        if sum(l[i:i + 2]) == 0:
            return True
    return False

# Test the function
test_sum_to_zero = is_sum_to_zero([1, 3, 5, 0])
test_sum_to_zero = is_sum_to_zero([1, 3, -2, 1])
test_sum_to_zero = is_sum_to_zero([1, 2, 3, 7])
test_sum_to_zero = is_sum_to_zero([2, 4, -5, 3, 9, 7])
test_sum_to_zero = is_sum_to_zero([1])

print("Result: ",test_sum_to_zero)
```
The function is_sum_to_zero takes a list l as input and returns True if there are three distinct elements in the list that sum to zero, and False otherwise. The function uses a loop to iterate over the list, with each iteration checking if the sum of the elements from the current sublist is equal to zero. The function then returns True if the condition is met, and False otherwise.

The script then tests the function by calling it with a list of different values and prints the result.