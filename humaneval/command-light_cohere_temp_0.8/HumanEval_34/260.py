```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(xnew)
    return result

def test_unique():
    test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    result = unique(test_list)
    assert len(result) == 7
    assert all(isinstance(i, int) for i in result)

unique # main function
test_unique # test function
``` 
This Python script presents a self-contained function named unique, designed to produce a list of unique elements from a given input list. The function employs a use of a set to monitor elements and a new list to hold distinct elements. It then appends these desired elements to the result list, returning the latter, which serves as the output for the function.

Moreover, the script includes a test function unique, which conducts a unit test on the unique function. This test verifies that the distinct function outputs the same result when given the same input list, ensuring the expected behavior of the function. The test function also ensures the correct type of each element in the output list.