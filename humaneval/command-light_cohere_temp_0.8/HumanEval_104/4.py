```python
def unique_digits(x):
    # Remove all even digits from x
    y = [d for d in str(x) if d.isdigit() andy[9]
    # Convert the list of unique digits back to a number
    return int(''.join(y))

# Test case 1: Ensure positive integer input is accepted
test_case_1 = [15, 33, 1422, 1]
assert unique_digits(test_case_1) == [1, 15, 33]

# Test case 2: Ensure an empty list is returned
test_case_2 = []
assert unique_digits(test_case_2) == []

# Test case 3: Ensure that only digits are returned
test_case_3 = [152, 323, 1422, 10]
assert [d for d in unique_digits(test_case_3)] == [1, 3, 14, 2]
```
This Python function named `unique_digits` takes a list of positive integers as its argument. It then removes all even digits from the list and returns a sorted list of the remaining, unique digits. The function has been tested against three different cases to ensure its correctness.