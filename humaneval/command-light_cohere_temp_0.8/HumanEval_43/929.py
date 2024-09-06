```python
def pairs_sum_to_zero(l):
    return any(sum(x) <= 0 for x in l)

# Test the function with various lists
for test_list in [[1, 3, 5], [-2, 1], [2, 4, -5], [1, 2, 3, 7]]:
    result = pairs_sum_to_zero(test_list)
    if result:
        print(f"List {test_list} passes the test.")
    else:
        print(f"List {test_list} fails the test.")

```
The code defines the function pairs_sum_to_zero that takes a list l of integers as input and returns True if there are two distinct elements in the list whose sum is zero, and False otherwise. It uses thenn's mathematical function 'any' to check for the condition that the sum of any two distinct elements in the list is less than or equal to zero.