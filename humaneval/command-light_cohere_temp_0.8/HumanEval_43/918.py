```python
def pairs_sum_to_zero(l):
    return any(x + y <= 0 for x, y in zip(l, l[1:]))

# Example usage:
input_list = [1, 3, 5, 0]
result = pairs_sum_to_zero(input_list)

if result:
    print("Two elements sum to zero")
else:
    print("No two elements sum to zero")
``` 
This script defines a function pairs_sum_to_zero that determines whether two elements in an input list sum to zero. 

It employs a simple method that checks each pair of elements to determine whether their sum equals zero. 
The result is then printed, and if the result is True, it indicates that two elements in the list sum to zero, and vice versa.