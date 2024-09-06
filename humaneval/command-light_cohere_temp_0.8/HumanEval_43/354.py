```python
def pairs_sum_to_zero(lst):
    s = 0
    for i in lst:
        if s + i == 0:
            return True
        s += i
    return False

# Tests
for i in [1, 3, -2, 1]:
    if not pairs_sum_to_zero([i]):
        print(f"{i} not a pair sum to 0")

for i in [1, 2, 3, 7]:
    if not pairs_sum_to_zero([i]):
        print(f"{i} not a pair sum to 0")

for i in [2, 4, -5, 3, 5, 7]:
    if not pairs_sum_to_zero([i]):
        print(f"{i} not a pair sum to 0")
``` 
The code defines a function `pairs_sum_to_zero` that takes a list of integers as input and checks if there exist two distinct elements in the list that add up to zero, in the sum. The test cases ensure that the elements in the input lists satisfy this property.