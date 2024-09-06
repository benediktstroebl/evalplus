```python
def pairs_sum_to_zero(lst):
    sum_of_two_numbers = lst[0] + lst[1]
    if sum_of_two_numbers == 0:
        return True
    else:
        return False

# Test the function
for i in range(0,10):
    actual_result = pairs_sum_to_zero([i, i+1])
    print(f"{i} -> {actual_result}")
``` 
The function uses the sum of the first two elements in the list to determine if it passes or not the test.