```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```

The function utilizes a list comprehension with a condition stating `x > 0` to filter out all positive numbers from the list. This ensures that only those numbers that are greater than zero are retained. 

To test the functionality of the solution, you can create a list of inputs of your choice and compare the expected output with the output produced by the function. 

For example, let's test the solution using the following input list:
```python
test_list = [11, -4, -15, 0, -8, 7, 34, -10, 12, -2, -20]
print(get_positive(test_list))  # Expected Output: [7, 34, 12]
``` 
This should output the list `[7, 34, 12]`, which contains only the positive numbers from the input list. 

The solution will effectively identify and return positive numbers from various input lists, ensuring you receive the desired output.