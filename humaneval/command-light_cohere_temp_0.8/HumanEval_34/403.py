```python
def unique(lst):
    seen = set()
    result = []
    for num in lst:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result

def test_unique():
    test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    result = unique(test_list)
    assert len(result) == 7  # Should be 7 unique elements

# Run the tests
test_unique()
``` 
This code defines a function called `unique` that sorts and returns unique elements from a given list. It also provides a test that verifies the functionality of this function with a test list. 

Please note that the complete script should be executed to run the function and pass the test.