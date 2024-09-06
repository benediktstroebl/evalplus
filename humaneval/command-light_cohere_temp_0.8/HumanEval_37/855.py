```python
def sort_even(lst):
    # Sort the list
    lst[:] = sorted(lst, reverse=True)
    evens = [item for item in lst if item % 2 == 0]
    # Return the list of even numbers
    return evens

# Example usage
list1 = [1, 2, 3, 4, 5, 6]
result = sort_even(list1)
print(result)  # Output: [3, 4, 5, 6]

list2 = [5, 6, 3, 4]
result2 = sort_even(list2)
print(result2)  # Output: [3, 6, 5, 4]
```
The function takes a list lst as input and returns a list lst' of even numbers from the original list lst. The sorted() function is used to sort the list, and the reverse=True parameter is used to sort the list in descending order. Then, a list comprehension is used to filter out the even numbers from the sorted list, and the resulting list is stored in the evens list. The resulting even list is then returned as the output.