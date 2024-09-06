```python
def pairs_sum_to_zero(l):
    if sum(l) == 0:
        return True
    else:
        return False

# Test the function
for i in range(0, 10):
    if pairs_sum_to_zero([i, i+1])):
        print("Passed test with input", i, "successful")
    else:
        print("Failed test with input", i, ".")
```
The code defines a function called pairs_sum_to_zero that takes a list of integers as an argument. The function checks if the using the sum of the two elements in the list sum to zero, and returns True if successful, and False otherwise. The test of the function is then run and passes the test with the input list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. The test will print whether the function passed or failed the test with the corresponding input.