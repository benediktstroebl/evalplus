```python
def by_length(arr):
    sorted_arr = sorted(arr)[::-1]
    transf_map = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    result = [transf_map[int(num) - 1] for num in sorted_arr if 1 <= int(num) <= 9]
    return result if result else []
```

The following tests will confirm that the function behaves as expected:
```python
test_1 = [[2, 1, 1, 4, 5, 8, 2, 3], ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']]
test_2 = [[], []]
test_3 = [55, 'Five']
test_4 = [1, -1, 55]
test_list = [test_1, test_2, test_3, test_4]

for t in test_list:
    assert by_length(t[0]) == t[1]
``` 

This problem can be solved by sorting the array and reversing it, and then using the indices of the sorted array to map the digits to their names. Strange numbers are ignored in the process.