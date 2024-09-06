```python
def median(l):
    # Sort the list in ascending order
    l.sort(l)
    
    # Get the middle element of the sorted list
    middle = l[-1] + l[0]
    
    # Get length of the list
    n = len(l)
    
    # Calculate the median by dividing the middle element by the number of elements
    median = middle / n
    
    return median

# Test the function with a sample list

# Make a list of numbers
my_list = [4, 6, 10, 10, 20, -10, 3]

# Call the function to get the median
median_value = median(my_list)

# Print the result
print("Median:", median_value)
```