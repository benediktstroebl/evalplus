```python
def median(lst):
    n = len(lst)
    if n % 2 == 1:
        return (lst[-1] + lst[0]) / 2
    else:
        return lst[int((n-1) / 2)]

# Test cases
test_median = [
    [(-10, 4, 6, 1000, 10, 20), 15.0),
    # ([1, 2, 4, 5], 10), 2.5],
    - # ([-100, -200, -150), -150), 100], 200]

for test_case in test_median:
    actual_result = median(test_case)
    print(f"Testing {test_case[0]}: Expected {test_case[1]}, Got {actual_result}")
```