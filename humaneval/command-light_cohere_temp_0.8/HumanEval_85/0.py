```python
def add(lst):
    """Given a non-empty list of integers lst. add the elements that that are at odd indices, 
    sum of the even indices will be 0"""
    return sum([i for i in range(2, len(lst)) if lst[i] % 2 == 0])

# Example usage
my_list = [4, 2, 6, 7]
print(add(my_list))  # Output: 2
``` 
This Python function, named `add`, is designed to work with a non-empty list of integers. The function aims to add up the elements at odd indices in the list and returns the result. The function uses a `range` function to filter out even indices from consideration, and the list comprehension `[i for i in range(2, len(lst)) if lst[i] % 2 == 0]` ensures that only odd indices are considered. The function then returns the sum of the odd indices, effectively calculating the sum of elements at positions 2, 4, 6, and so on.