```python
def unique_digits(x):
    """
    Sorts and returns a list of positive integers' unique even digits.
    """
    unique(x[0:])
    return list(map(int,filter(lambda x:x>0 and x%10==0, x))))

# Test the function
test_data = [15, 33, 1422, 1]
test_result = unique_digits(test_data)
print(test_result)

test_data2 = [152, 323, 1422, 10]
test_result2 = unique_digits(test_data2)
print(test_result2)
```
This code defines a function `unique_digits` that takes a list `x` of positive integers and returns a sorted list of unique even digits from those integers. The function uses the unique function from Python's standard library to filter out the unique even digits, then converts the result back to an integer list and returns it.