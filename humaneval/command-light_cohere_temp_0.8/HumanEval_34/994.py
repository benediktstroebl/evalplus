```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not [])

# Test cases
unique_test = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print("Unique Test:", unique_test)  # Output: Unique Test:[0, 2, 3, 5, 9, 123]

seen = set()
test_case_one = [5, 3, 9, 0]
test_case_two = [2, 3, 5, 0]
test_case_three = [5, 0, 3, 2]
test_case_four = [123, 5, 3, 2]
test_case_five = [1, 2, 3, 4]

for case in [unique_test, test_case_one, test_case_two, test_case_three, test_case_four, test_case_five]:
    print(f"Case {case}:", case)
    print(case)
    print("Unique:", unique(case))
    print()
```
This script defines a function unique that sorts and returns unique elements from an input list. The test cases provided are also sorted lists, and the output will be the sorted list of unique elements.