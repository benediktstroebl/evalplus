```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not ()]

# Test cases
test_data = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_result = unique(test_data)
print("Test 1:", test_result)  

test_data2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
test_result2 = unique(test_data2)
print("Test 2:", test_result2) 
```  This Python code defines a function called unique, designed to return a list of unique elements from an input list lst. The function utilizes a unique nature of sets to track elements that have been encountered, ensuring only distinct elements are returned. The code then includes two test cases, each featuring a list of numbers. The unique function is applied to each test case, and the results are displayed.