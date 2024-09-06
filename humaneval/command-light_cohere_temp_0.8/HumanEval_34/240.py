```python
def unique(l: list):
    return list(set(l))

# Test the function
def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

# Run the test and print the result
test_unique()
print("Unique function passed all tests!")
```
This code defines a function unique that takes a list l as input and returns a list of unique elements from the input list, using the set() function to remove duplicates. It also has a test_unique, which passes the test for the unique function with a sample list. The code then prints a result, indicating that the function passed all the tests.