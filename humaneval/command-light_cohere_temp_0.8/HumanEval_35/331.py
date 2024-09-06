```python
def max_element(lst):
    return max(lst)

# Test the max_element function
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Test with list of strings
assert max_element(["hello", "world!pants", "!code"]) == "world.pants"
 example:
    def getMaxElement(lst):
        # Use built-in max function to get the highest element in the list
        return max(lst)

# Test the function with a list of mixed data types
assert getMaxElement([1, 2, 3, -5, 'hello']) == 3

# Test error handling with invalid input
try:
    getMaxElement([1, 2, 3, 'invalid'])
except TypeError:
    print("Error: Invalid input.input.input")
``` 
This code includes the function definition, unit tests, and additional test cases to cover various scenarios.