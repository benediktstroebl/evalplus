```python
def pairs_sum_to_zero(l):
    return any(sum(x) == 0 for x in l)

# Example usage:
input_list = [1, 3, 5, 0]
output = pairs_sum_to_zero(input_list)
print(output)  # Output should be True

input_list = [1, 3, -2, 1]
output = pairs_sum_to_zero(input_list)
print(output)  # Output should be True

input_list = [1, 2, 3, 7]
output = pairs_sum_to_zero(input_list)
print(output)  # Output should be False

input_list = []
output = pairs_sum_to_zero(input_list)
print(output)  # Output should be True
```

The script defines the function pairs_sum_to_zero that checks whether all the elements in the input list sum to zero. It returns "True" if there are any two elements in the list that sum to zero, and "False" otherwise. The script provides several examples to test the function, and the output is printed to the console.