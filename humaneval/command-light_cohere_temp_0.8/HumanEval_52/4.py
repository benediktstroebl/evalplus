```python
def below_threshold(lst, threshold):
    return all([x <= threshold for x in lst])

# Test the function
tests = [ [ [1, 20, 4, 10], 100 ]
threshold = 5
result = below_threshold(tests, threshold)
print(result)  # Output: False
``` 
This script defines a function below_threshold that checks whether all numbers in a given list lst are less than or equal to a given threshold. It uses the simple list comprehension with a lambda function to achieve this.  The function then returns True if all elements in the list are below the threshold, and False otherwise.