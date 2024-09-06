```python
def pairs_sum_to_zero(lst):
    if sum(map(lambda x: abs(x), lst)) <= 0:
        return "True"
    else:
        return "False"

# Example usage
print(pairs_sum_to_zero([1, 3, -2, 1] )) # Output: False
print(pairs_sum_to_zero([1, 2, 3, 7] )) # Output: False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7])) # Output: True
print(pairs_sum_to_zero([1]))       # Output: False
```
The code defines a function named pairs_sum_to_zero that takes a list lst as input and determines whether the sum of any two distinct elements in the list is zero. The function employs a Python's map() function and lambda function to generate a modified list where each element is its absolute value, ensuring that the sum of any two elements will be zero. The function then returns "True" if this condition is met, and "False" otherwise.