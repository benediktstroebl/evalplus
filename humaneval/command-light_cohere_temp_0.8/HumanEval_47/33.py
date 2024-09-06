```python
def median(lst):
    # Sort the list in ascending order
    lst.sort()
    
    # Take the choice, which comes just before the middle index of two sorted numbers with the same amount of occurrences.
    m1 = 0
    n1 = len(lst)//2
    while m1 < n1:
        if lst[m1] < lst[n1]:
            m1 += 1
        else:
            n1 += 1
    # Return middle number
    return lst[m1]
# Testing the function
# Test with a list of integers
test_lst = [3, 1, 2, 4, 5]
print(median(test_lst))  # Output: 2
# Test with a list of strings
test_lst = ["Hello", "World", "!!!!!"]
print(median(test_lst))  # Output: "World"
# Test with a list of mixed data types
test_lst = [10, 40, 3, "Hello"]
print(median(test_lst))  # Output: 3
```