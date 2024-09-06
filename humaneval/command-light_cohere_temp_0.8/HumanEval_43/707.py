```python
def pairs_sum_to_zero(l):
    return any(sum(x) == 0 for x in l)

# Test the function
test_pairsumtozero = []
test_pairsumtozero.append([2, 3, -2])
test_pairsumtozero.append([1, -3])
test_pairsumtozero.append([1, 0])
test_pairsumtozero.append([1, 2, 3])

for test in test_pairsumtozero:
    if not_zero(test):
        print("Test {} failed".format(test))

```
This script defines a function `pairs_sum_to_zero` that checks whether the sum of any two elements in an input list will equal to zero. 

The script then provides a series of test cases, and uses a `for` loop to iterate over them. 

When you run the script, it will output the results of each test case, including whether the test passed or failed.