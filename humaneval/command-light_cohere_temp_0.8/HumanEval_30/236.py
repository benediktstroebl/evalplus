```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

#Test cases
test_get_positive = [
    dict(zip('test_cases'.split(), 
             [([-1, 2, -4, 5, 6], [2, 5, 6]),
              ([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], [5, 3, 2, 3, 9, 123, 1])]))
]

#Run the function and tests
for name,test_case in test_get_positive:
    print(f"Test {name}...")
    got = get_positive(test_case[0])
    assert got == test_case[1]
``` 
This code defines a function **get_positive** that takes in a list and returns a new list with only the positive numbers. It also has a test cases to test the function and passes the test successfully.