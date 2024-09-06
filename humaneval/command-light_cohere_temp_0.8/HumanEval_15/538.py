```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n}{' ' * (n - 1)}".format()

# Test case 1
test_case1 = int(input())
if test_case1 == len(string_sequence(test_case1)):
    print("Test case 1 passed")
else:
    print("Test case 1 failed")

# Test case 2
test_case2 = 10
if len(string_sequence(test_case2)) == test_case2:
    print("Test case 2 passed")
else:
    print("Test case 2 failed")

# Test case 3
test_case3 = 0
test_case4 = 100
test_case5 = None

if all(test_case3, test_case4, test_case5) == tuple(map(int, input().
(string_sequence, [test_case3, test_case4, test_case5])):
    print("Test case 3-4-5 passed")
else:
    print("Test case 3-4-5 failed")
```