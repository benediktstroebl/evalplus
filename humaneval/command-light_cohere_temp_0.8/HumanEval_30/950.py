```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test the function with a list containing a mix of numbers (both positive and negative)
list1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
# Test with another list with only positive numbers
list2 = [2, 5, 6]

result1 = get_positive(list1)
result2 = get_positive(list2)

print("List 1:", result1)
print("List 2:", result2)

# Test with a list containing only positive numbers
list3 = [2, 5, 6, 7, 8, 9]
result3 = get_positive(list3)

print("List3:", result3)
``` 
This script defines the `get_positive` function that takes a list as input and returns a new list with only the positive numbers from the original list. It then passes this tests the 2 test cases and prints the results.