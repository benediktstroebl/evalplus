```python
def filter_integers(values): 
    return [x for x in values if isinstance(x, int)]

# Test cases
values1 = ['a', 3.14, 5]
values2 = [1, 2, 3, 'abc', {}, []]

print("Test case 1:", values1)
print(" ->", filter_integers(values1))

print("\nTest case 2:")
print(" ->", values2)
print("Expected Output:", [1, 2, 3])

``` 
This code defines a function called **filter_integers** that takes a list of values as an argument and returns a new list containing only the integers from the input list. It uses the _ filtering technique to remove non-integer elements from the input list and returns the resulting filtered list. The test cases demonstrate the to test the correctness of the function, the output of the function is then printed to compare it with the expected output. 

This code follows the DRY principle of writing, which aims to avoid code duplication and promote clean, efficient, and maintainable code.