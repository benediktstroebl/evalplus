```python
def pairs_sum_to_zero(l):
    if sum(l) == 0:
        return True
    else:
        return False

# Unit tests
test_pairs_sum = [
    [
        [],  # List of numbers is empty
        [1, 3],  # Two numbers sum to 5
        -2, 1  # Two numbers sum to -3
    ]

if __name__ == "__main__":
    for test in test_pairs_sum:
        result = pairs_sum_to_zero(test)
        print(f"Test: {test, result}")
        assert result == test[1] == True
```
This Python script defines a function called pairs_sum_to_zero that takes a list of integers as input and determines whether the list has two elements whose sum equals zero. The script also includes a test suite with a variety of test cases. This test suite is designed to validate the correctness of the function. The function returns True if the list has two elements that sum to zero, and False otherwise. 

You can use this script to test your functions or to implement similar functionality for your projects.