```python
def specialFilter(nums):
    oddFirst = lambda x: x[0] % 2 != 0
    oddLast = lambda x: x[-1] % 2 != 0
    return sum(n for n in nums if oddFirst(n) and oddLast(n) and n > 10)
```

The code uses a generator expression to filter non-compliant numbers and then counts the elements with a sum function. This avoids creating a list from the entire array, ensuring efficiency. 

The lambda functions `oddFirst` and `oddLast` are used to filter out numbers that do not comply with the problem statement. 

To verify the accuracy of the solution, you can create a test case like this:
```python
test_cases = [
    [15, -73, 14, -15, 33, -2, -3, 45, 21, 109],
    [154, 59, 251, 199, 593, 796, 863, 577, 713, 919],
    [104, -33, -55, -77, -99, 33, 55, 77, 99, 104],
]

expected_results = [1, 2, 0]

for test, expected in zip(test_cases, expected_results):
    result = specialFilter(test)
    assert result == expected, f"For input {test}, expected {expected} but got {result}"
```

This way, you can validate the correctness of the solution with different test cases. 
If you want to optimize the code to be more efficient and readable you can do it as follows:
```python
def specialFilter(nums):
    """
    Returns the number of elements in the array that are greater than 10 and both first and last digits are odd.
    """
    def is_odd(num):
        return num % 2 != 0

    filtered_nums = [num for num in nums if is_odd(num[0]) and is_odd(num[-1]) and num > 10]
    return len(filtered_nums)
```

This version of the code uses a more descriptive approach, the lambda functions were replaced with named functions to define the filtering behavior, for both the first and last digits of the numbers. 

Additionally, instead of using the sum function to count the elements, we used `filtered_nums` to directly return the `len` of the filtered list. 

This makes the code more readable and maintainable, especially if you need to apply additional logic to the filtered list.