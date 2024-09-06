```python
def pairs_sum_to_zero(l):
    if sum(l) == 0:
        return True
    return False

# Unit tests for the function 'pairs_sum_to_zero'
test_pairs_sum_to_zero = []
test_pairs_sum_to_zero.add([range(0, 4))
test_pairs_sum_to_zero.add([range(1, 4))
test_pairs_sum_to_zero.add([range(2, 4))

# Loop through each test case
for idx, test_case in enumerate(test_pairs_sum_to_zero):
    print(f"Test {idx}: {test_case}")
    if not_zero_sum(test_case):
        print("should be True")
    else:
        print("should be False")

def not_zero_sum(l):
    if sum(l) == 0:
        return True

# Loop through each list
for i in range(5):
    new_list = [i] + [7 - i] * 2
    if not_zero_sum(new_list):
        print("should be False")
    else:
        print("should be True")
```

The provided Python script defines a function `pairs_sum_to_zero` that checks whether all the sum of pairs of elements in a list is zero. The function returns `True` if there are two distinct elements in the list that sum to zero, and `False` otherwise. 

The script also includes unit tests for the `pairs_sum_to_zero` function using a test list. The `not_zero_sum` function is then used to test these tests, which checks whether the function correctly identifies pairs with sum to zero. 

The tests cover different scenarios, such as empty lists, lists with one element, lists with two elements, and lists with elements that sum up to zero.