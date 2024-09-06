```python
def triples_sum_to_zero(lst):
    # Initialize variables
    sum_is_zero = False
    sum_is_positive = False
    sum_is_negative = False
    sum_is_odd = False
    sum_value = sum(lst)
    
    # Check if all elements in the list sum to zero
    if sum_value == 0:
        return "All elements sum to zero!"
    elif sum_value < 0:
        sum_is_negative = True
    else:
        sum_is_positive = True
    
    # Check if any odd number in the list
    odd = [x for x in lst if x % 2 == 1]
    if odd:
        sum_is_odd = True
    
    # Check if any element in the list is greater than 1
    greater = [x for x in lst if x > 1]
    if greater:
        sum_is_positive = False
    
    # If all elements sum to a positive number, return False
    if sum_is_positive:
        return "Not all elements sum to zero!"
    
    return "Three distinct elements sum to zero."

# Example usage
my_list = [1, 3, 5, 0]
result = triples_sum_to_zero(my_list)
print(result)  # Output: True
```