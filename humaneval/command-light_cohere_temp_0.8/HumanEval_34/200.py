```python
def unique(lst):
    seen = set()
    result = []
    for num in lst:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result

# Test cases
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_result = unique(test_list)
print("Test list:", test_list)
print("Test result:", test_result)

empty_list = []
test_empty = unique(empty_list)
print("Empty list:", empty_list)
print("Test empty result:", test_empty)

list1 = [1, 2, 3, 4, 5, 6]
test_list1 = [1, 2, 3, 4, 5, 6]
test_result1 = unique(test_list1)
print("List1:", list1)
print("Test result1:", test_result1)

complex_list = [1, 2, 3 + 1, 3, 4 + 2, 5]
test_complex = unique(complex_list)
print("Complex list:", complex_list)
print("Test result2:", test_complex)
```

This Python code defines a function `unique` that returns a list containing unique elements from a given list. It uses a `seen` set to keep track of encountered elements and a new list `result` to collect unique elements. The function iterates through each element in the input list and checks if the element is already in the `seen` set. It then adds the this element to the result list and the `seen` set. The function returns the result.

The code also provides several test cases to demonstrate the usage of the `unique` function. The test cases include lists with different elements, empty lists, and complex lists with elements containing variables.