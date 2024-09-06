```python
def sort_even(lst):
    # Filter out odd index numbers
    odd = [i for i in range(len(lst)) if lst[i] % 2 == 1]
    # Sort the even index numbers to the front of the list
    lst[:odd] = lst[odd].sort()
    # Copy the sorted list to the original list to maintain the order
    lst = lst[:] + lst[odd:]
    return lst

# Test case 1
test_list = [1, 2, 3]
result = sort_even(test_list)
print("Test Case 1 Result:", result)

# Test case 2
test_list = [5, 6, 3, 4]
result = sort_even(test_list)
print("Test Case 2 Result:", result)

# Test case 3
test_list = [1, 3, 2, 4, 5, 6]
result = sort_even(test_list)
print("Test Case 3 Result:", result)
```
The function `sort_even` sorts a list such that even index numbers appear first, and the original order is otherwise preserved. The test cases demonstrate the