```python
def incr_list(lst):
    lst[0] = 1
    return lst

# Test case 1
test_cases = [
    [1, 2, 3],
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [6, 7, 8],
]

test_results = []
for test_case in test_cases:
    test_result = incr_list(test_case)
    test_results.append(test_result)

# Test case 2
def test_function():
    l = [1, 2, 3]
    incr_list(l)

# Test case 3
def test_function2():
    l = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    incr_list(l)

if test_results[0][0] == test_results[1][0]:
    print("Test case 1 passed.")
elif test_results[0][1] == test_results[1][1]:
    print("Test case 1 failed.")
else:
    print("Something went wrong.")

if test_results[2][0] == test_results[2][1]:
    print("Test case 2 passed.")
elif test_results[2][0] != test_results[2][1]:
    print("Test case 2 failed.")
else:
    print("Something went wrong with test case 2.")

if test_results[3][0] == test_results[3][1]:
    print("Test case 3 passed.")
elif test_results[3][0] != test_results[3][1]:
    print("Test case 3 failed.")
else:
    print("Something went wrong with test case 3.")
```