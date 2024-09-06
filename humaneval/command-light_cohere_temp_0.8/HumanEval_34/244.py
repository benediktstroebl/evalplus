```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x unique)
    return result

# Test 1
test_cases = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result_test1 = unique(test_cases)
print("Test 1:", result_test1)

# Test 2
test_cases2 = [0, 1, 2, 3, 'abc', 5]
result_test2 = unique(test_cases2)
print("Test 2:", result_test2)

# Test 3
test_cases3 = [['a', 'bb', 'cc', 'dd']
result_test3 = unique(test_cases3)
print("Test 3:", result_test3)
``` 
This script defines a function unique that takes a list as an argument and returns a new list with unique elements from the original list. It uses a unique elements and sets to keep track of items seen so far, ensuring that duplicates are not added to the result.

The script then passes three test cases to the function and prints the results to the console.