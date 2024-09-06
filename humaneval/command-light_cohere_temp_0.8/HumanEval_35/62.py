```python
def max_element(lst):
    if not_positive(lst):
        return float('-inf')
    elif len(lst) == 0:
        return lst[0]
    else:
        return max(lst)

def not_positive(lst):
    return all(x > 0 for x in lst)

# Test cases
test_max_element = [
    [(-5, 'Should return negative infinity'),
     ([], 'Should return 0'),
     ([1, 2, 3], 'Should return 3'),
     ([5, 3, -5], 'Should return 5'),
     ([-3, 0, 2, -3], 'Should return 0'),
     ([1, 2, -3, 3], 'Should return 3'),
     ([-10, 123], 'Should return -10'),
     ([-100, -200], 'Should return -100')
]

# Execute tests and print results
for test, expected_result in test_max_element:
    if test != []:
        got_result = max_element(test)
        if got_result != expected_result:
            print(f"Test {test} failed. Expected: {expected_result}, Got {got_result}")
 ```