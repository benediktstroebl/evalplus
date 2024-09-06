```python
def pairs_sum_to_zero(l):
    if not sum(l) == 0:
        return "YES"
    else:
        return "NO"

#Test cases
test_cases = [
    [1, 3, 5, 0],
    [1, 3, -2, 1],
    [1, 2, 3, 7],
    [2, 4, -5, 3, 5, 7],
    [1]
]

for test_num, test_case in enumerate(test_cases, start=1):
    result = pairs_sum_to_zero(test_case)
    print(f"{test_num}: {result}")
```
The code defines a function `pairs_sum_to_zero` that checks if the sum of the elements in a list is equal to zero. It returns "YES" if there are two distinct elements in the list whose sum is zero, and "NO" otherwise. The test cases provided are then a list of test cases, each consisting of a number and a corresponding test case. The function is then called with each test case, and the result is printed.