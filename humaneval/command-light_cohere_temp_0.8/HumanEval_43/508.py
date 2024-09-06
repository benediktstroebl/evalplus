```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    list comprehension is a simple method to determine if the sum of two elements in the list is zero or not.
    """
    number pairs in the list that sum to zero, and return True
    """
    return any([sum(x, y) <= 0 for x, y in zip(l, l[1:]))

# Example usage:
test_list = [1, 3, 5, 0, 1, 2, 3, 7]
result = pairs_sum_to_zero(test_list)
print(result)
```

The provided Python script defines a function called pairs_sum_to_zero, which aims to determine if there are pairs of numbers in an input list whose sum equals zero. The function achieves this using a list comprehension approach, it iterates through the list and checks if the sum of any pair of consecutive elements equals zero. The function then returns True if this condition is met, indicating that there are two distinct elements in the list whose sum equals zero, and False otherwise. The test_list is provided as an sample to demonstrate the usage of the function, and the output is printed to the console.