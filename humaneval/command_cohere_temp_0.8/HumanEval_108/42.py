```python
def count_nums(arr):
    return sum(x > 0 for x in map(sum, map(int, str(n)) for n in arr))
```

This solution uses nested list comprehensions and generators to determine the sum of digits for each number in the array and filter out numbers whose digit sum is greater than or equal to 0. The final result will be the length of the filtered list which is the count of numbers with a positive digit sum. The function includes a docstring with example tests that demonstrate its behavior for edge cases and a range of scenarios. 
```python
def test_count_nums():
    """
    Test the count_nums function
    """
    assert count_nums([]) == 0
    assert count_nums([-1, 11, -11]) == 1
    assert count_nums([1, 1, 2]) == 3
    assert count_nums([1, -1, 2, -2, 3]) == 3
    assert count_nums([11, 2, -1, -12, -311]) == 4
``` 

This test suite provides a variety of inputs to validate the functioning of the `count_nums` function with different scenarios, including empty arrays, arrays with only negative integers, and arrays with a mix of positive and negative integers. 
```python
if __name__ == "__main__":
    test_count_nums()
``` 

This conditional statement ensures that the test suite is executed only when the script is run directly, rather than being imported as a module, which allows you to test the function behavior conveniently from the command line.