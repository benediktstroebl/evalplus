```python
def by_length(arr):
    sorted_arr = sorted(arr)[::-1]
    transf_map = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    result = [transf_map[int(num)] for num in sorted_arr if 1 <= int(num) <= 9]
    return result if result else []
```

The provided Python script defines a function `by_length` that takes an array of integers as input and sorts integers between 1 and 9 inclusive, reverses the sorted array, and then transforms each digit into its corresponding name from the `transf_map` list. The function returns the transformed array if it's not empty, or an empty array if the input array is empty. Additionally, any unusual numbers are ignored in the process. This solution is self-contained and can be directly used to solve the problem as it includes the transformation mapping within the script.

This code can be tested as follows:
```python
TEST_CASES = [
    ([2, 1, 1, 4, 5, 8, 2, 3], ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']),
    ([]                  , []),
    ([1, -1, 55]        , ['One']),
    (['a', 'b', 'c']    , [])
]

for test_case in TEST_CASES:
    assert by_length(test_case[0]) == test_case[1]
```