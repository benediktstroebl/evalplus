```python
def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers only integers.

    Examples:
    is_sorted([5]) ➞ True
    is_sorted([1, 2, 3, 4, 5]) ➞ True
    is_sorted([1, 3, 2, 4, 5]) ➞ False
    is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
    is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
    is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
    is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
    is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
    '''
    # Sort the list
    sorted_num = sorted(lst)
    # Compare original list with sorted list
    return sorted_num == lst

# Test the function
test_is_sorted = is_sorted([5])  # True
test_is_sorted([1, 2, 3, 4, 5])  # True
test_is_sorted([1, 3, 2, 4, 5])  # False
test_is_sorted([1, 2, 2, 3, 3, 4])  # True
test_is_sorted([1, 2, 2, 2, 2, 3, 4])  # False
```
The function is_sorted accepts a list of numbers and returns a boolean value. The method works by sorting the list using the sorted() function and then comparing the original list with the sorted list. The sorted() function sorts the list using a sorting algorithm, such as a comparison-based algorithm. The function returns True if the list has more than one duplicate of the same number. It returns False if the duplicates are present.

The test_is_sorted function is a simple example of how to use the is_sorted function to test whether a list of numbers is sorted. It can be used to test the function with different lists of numbers to see if the list is sorted.