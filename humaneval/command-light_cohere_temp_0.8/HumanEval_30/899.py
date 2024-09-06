```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

# Test the function with a list containing various numbers
test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
result = get_positive(test_list)
print(result)  # Expected output: [2, 3, 2, 3, 9, 123, 1]
``` 
This Python script defines a function get_positive that takes a list l as input and returns a new list containing only the positive numbers from l. The function is tested with a sample list using the test_list, and the result is printed to verify the correctness of the function.