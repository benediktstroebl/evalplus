```python
def sort_even(lst):
    return sorted(lst, key=lambda x: x if x % 2 == 0 else x + 1)

# Example usage:
input_list = [1, 2, 3, 4, 5, 6]
result = sort_even(input_list)
print(result)

input_list2 = [5, 6, 3, 4]
result2 = sort_even(input_list2)
print(result2)
```
This script defines a function `sort_even` that sorts a list according to even values. It uses the `key` parameter to specify a lambda function to determine the sorting key. The output of the lists are then printed to show that the function works as expected.