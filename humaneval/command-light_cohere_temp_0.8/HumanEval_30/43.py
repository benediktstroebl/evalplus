```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test the function
test_get_positive = []
test_get_positive.push([-1, 2, -4, 5, 6])
test_get_positive.push([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])

print("List with negative numbers: ", end="")
for item in test_get_positive:
    print("-", end="")
print()

print("List with positive numbers:", end="")
res = get_positive(test_get_positive)
print(res)

# Test the function with mixed list
test_mixed = []
test_mixed.push([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
test_mixed.push([5])

res = get_positive(test_mixed)
print("List with mixed numbers:", end="")
print(res)
``` 
This script defines a function, `get_positive`, which takes a list as an argument and returns a new list containing only the positive numbers from the original list. It is then test the script that this function can correctly handle both positive and negative numbers within the passed list.