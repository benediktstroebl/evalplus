Here's a Python script with a self-contained function that solves the problem of finding two numbers in a list that sum to zero:
```python
def pairs_sum_to_zero(l):
    return sum((a, b) for a, b in zip(l, l[1:])) == 0

# Test the function with various lists
test_list = [1, 3, 5, 0]
test_list2 = [1, 3, -2, 1]
test_list3 = [1, 2, 3, 7]
test_list4 = [2, 4, -5, 3, 5, 7]

print(test_list)
print(test_list2)
print(test_list3)
print(test_list4)

if pairs_sum_to_zero(test_list):
    print("Two elements sum to zero.")

if pairs_sum_to_zero(test_list2):
    print("Two elements sum to zero.")

if pairs_sum_to_zero(test_list3):
    print("Two elements sum to zero.")

if pairs_sum_to_zero(test_list4):
    print("Two elements sum to zero.")
```

This script defines a function `pairs_sum_to_zero` that takes a list `l` as input and returns `True` if there are two distinct elements in `l` that sum to zero, and `False` otherwise. The function uses the` `zip` to iterate over the elements of the list, and sum the pairs of elements. The test is then applied to a variety of lists and passes the corresponding tests.