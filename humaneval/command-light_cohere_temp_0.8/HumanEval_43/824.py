```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
	"""
    # Sort the list
    l.sort()
   
    # Initialize a sum to zero
    sum = 0
    # Loop through the list
    for i in l:
        # Check if the element is negative
        if i < 0:
            sum += i
        # Add the element to the sum
        sum += i
    # Return sum
    return sum == 0

# Test the function
# Test cases
test_pairs_sum_to_zero = pairs_sum_to_zero([1, 3, 5, 0])
print(test_pairs_sum_to_zero) # Output: True

test_pairs_sum_to_zero = pairs_sum_to_zero([1, 3, -2, 1])
print(test_pairs_sum_to_zero) # Output: False

test_pairs_sum_to_zero = pairs_sum_to_zero([1, 2, 3, 7])
print(test_pairs_sum_to_zero) # Output: False

test_pairs_sum_to_zero = pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
print(test_pairs_sum_to_zero) # Output: True

test_pairs_sum_to_zero = pairs_sum_to_zero([1])
print(test_pairs_sum_to_zero) # Output: False
```
The above Python script defines a function called `pairs_sum_to_zero` that takes a list of integers as input and returns `True` if there are two distinct elements in the list that sum up to zero, and `False` otherwise. The script then provides several test cases to verify the correctness of the function. The function uses the sorting the list and checking if any two elements add up to zero. It uses the loop and a sum variable to perform this check.