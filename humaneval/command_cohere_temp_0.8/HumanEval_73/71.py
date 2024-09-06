```python
def smallest_change(arr):
    arr = list(set(arr))
    return sum([1 for i in range(len(arr)) if arr[i] != arr[len(arr) - 1 - i]])
```

The function `smallest_change` takes an array `arr` as input and returns the minimum number of elements that need to be changed to make the array palindromic. It utilizes the set method to remove duplicate elements within the array and then checks if each element is equal to the corresponding element in the reverse order within the array. Elements that are not equal require a change to make the array palindromic.

Here is a test case to test the function:
```python
test_cases = [[1, 2, 3, 5, 4, 7, 9, 6], [1, 2, 3, 4, 3, 2, 2], [1, 2, 3, 2, 1]]

expected_results = [4, 1, 0]

for i in range(len(test_cases)):
    print(f'Test Case: {test_cases[i]}, Expected: {expected_results[i]}')
    result = smallest_change(test_cases[i])
    print(f'Result: {result}')
    assert result == expected_results[i]
```