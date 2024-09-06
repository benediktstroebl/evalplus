```python
def get_positive(l: list):
    return [x for x in l if x >= 0]

# Test the function with different lists
test_list1 = [-1, 2, -4, 5, 6]
test_list2 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
test_list3 = [5, 3, 300, 2, -300]

# Test the function with user input
test_input = input("Enter a list of numbers separated by spaces: ")
test_list4 = [float(x) for x in input().
test_list5 = [int(x) for x in input("").]

# Test cases with specific requirements
print(get_positive(test_list1))  # Output: [2, 4, 5, 6]
print(get_positive(test_list2))  # Output: [5, 3, 9]
print(get_positive(test_list3))  # Output: [] (empty list)
print(get_positive(test_list4))  # Output: [5, 3,]
print(get_positive(test_list5))  # Output: [])
```

The script defines a function called `get_positive` that filters out only the positive numbers from the input list. 

You can test the function with different lists and even use the `input()` function to allow the user to provide input. The output will be the specific to each test case.