```python
def odd_count(lst):
    r = []
    for digits in lst:
        counts = str(sum(1 for digit in digits if digit % 2 == 1))
        r.append(f"the number of odd elements in the string {counts} of the input")
    return r
```

This solution uses a simple loop to iterate through each string in the list and calculate the count of odd digits in each string. The resulting counts are appended to the result list after being formatted into a string, and the final result is returned. 

This solution is efficient and straightforward, but it's worth noting that odd_count doesn't handle an empty list gracefully, as it would raise an IndexError. Also, the unit tests for this code could benefit from more meaningful assertions to better illustrate the expected output. 

Here is a test case for the provided solution to illustrate the point:
```python
def test_odd_count():
    # Test list of strings with digits
    assert odd_count(['1234567']) == ["the number of odd elements in the string 4 of the input"]

    # Test list of strings with single digits
    assert odd_count(['3', "11111111"]) == ["the number of odd elements in the string 1 of the input", "the number of odd elements in the string 8 of the input"]

    # Test empty list
    assert odd_count([]) == []
```