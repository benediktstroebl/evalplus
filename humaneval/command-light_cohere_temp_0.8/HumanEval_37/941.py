```python
def sort_even(lst):
    # Initialize an empty list to store the sorted even numbers
    even_out = []
    
    # Loop through the list and append even numbers to the new even_out list
    for num in lst:
        if num % 2 == 0:
            even_out.append(num)
    
    # Return the list containing only even numbers
    return even_out

# Test case 1
print(sort_even([1, 2, 3]))
# Expected output: [1, 2, 3]

# Test case 2
print(sort_even([5, 6, 3, 4]))
# Expected output: [3, 6, 5, 4]

# Test case 3
print(sort_even([10, 2, 8, 9]))
# Expected output: [10, 2, 8, 9]
```

This Python code defines a function `sort_even` that sorts a list of numbers into one that only contains even numbers. The function first creates a empty list `even_out` and then loops through the original list, appending even numbers to `even_out`. Finally, it returns the new list that only contains even numbers. 

I hope this explanation helps clarify the functionality and purpose of your code!