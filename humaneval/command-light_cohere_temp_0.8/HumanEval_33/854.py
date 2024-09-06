```python
def sort_third(lst):
    """Sorts the list so that values that are not divisible by three are at the beginning and values that are divisible by three are at the end of the list"""
    # Sorting algorithm (quicksort) with a custom key function
    lst = sorted(lst, key=lambda x: x if x % 3 == 0 else x // 3)
    return lst

# Test cases
test_list = [1, 2, 3]
test_list2 = [5, 6, 3, 4, 8, 9, 2]

# Function call and print results
result_list = sort_third(test_list)
print("Sorted list with non-divisible thirds:")
print(result_list)

result_list2 = sort_third(test_list2)
print("Sorted list with divisible thirds:")
print(result_list2)
```
This Python script defines a function `sort_third` that sorts a list so that values not divisible by three are at the beginning and values divisible by three are at the end of the list. The algorithm used quicksort with a custom key function to achieve this. It provides two test cases to test the function and prints the results.