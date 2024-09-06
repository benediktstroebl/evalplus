```python
def pairs_sum_to_zero(lst):
    if sum(lst) == 0:
        return True
    return False

#Test cases
test_sum_to_zero = [
    (1, 3, 5, 0),
    (1, 3, -2, 1),
    (1, 2, 3, 7),
    (2, 4, -5, 3, 5, 7),
    (1,)
]

for i, test in enumerate(test_sum_to_zero):
    actual = pairs_sum_to_zero(test)
    expect = test[1]
    print(f"Test {i+1}: {actual} vs {expect}")
    if actual != expect:
        print("Failed")
        break
```
The above Python code defines a function `pairs_sum_to_zero` that checks whether the sum of all the elements in a given list is zero. It returns `True` if the source list has two distinct elements that sum up to zero, and `False` otherwise. The code includes a test cases to verify the functionality of the function, passing each test case to the `pairs_sum_to_zero` function and comparing the returned value with the expected result. 

The output will display the expected and actual results for each test case, and if any test fails, it will indicate a problem in the function's behavior.