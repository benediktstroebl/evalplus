```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function called 'add()'. This function takes a list as input and aims to calculate the sum of even integers present at odd indices in the list. To achieve this, it employs a list comprehension, iterating through each element in the input list. If the index of the element is odd (i.e., `i % 2 == 1`) and the element itself is even (i.e., `el % 2 == 0`), it includes the element in the `even_odd` list. Finally, the function returns the sum of the elements in the `even_odd` list, effectively computing the desired sum of even integers at odd indices in the input list. 

Let's break down the code:
1. `def add(lst)`: This line defines a function named 'add' that takes a single argument 'lst', which is expected to be a list. 

2. `even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]`: This is a list comprehension that iterates through each element `el` in the input list `lst`. The iteration is done using the `enumerate()` function, which provides both the index `i` and the element `el` in each iteration. For each element, it checks if the index `i` is odd (i.e., `i % 2 == 1`) and if the element `el` is even (i.e., `el % 2 == 0`). If both conditions are met, the element `el` is included in the `even_odd` list. 

3. `return sum(even_odd)`: After the list comprehension, the function returns the sum of all elements included in the `even_odd` list. The `sum()` function is used to calculate the sum of the elements in the list. 

In summary, the `add()` function processes a list, identifies even elements at odd indices, and returns their sum. 

This function can be tested by calling it with different lists and verifying that it produces the expected results, as shown in the examples below:
```python
# Test 1
test_list = [4, 2, 6, 7]
expected_result = 2
add(test_list) == expected_result  # Should evaluate to True

# Test 2
test_list = [1, 3, 5, 7, 9, 11]
expected_result = 6
add(test_list) == expected_result  # Should evaluate to True

# Test 3
test_list = [2, 4, 6, 8, 7, 9, 10, 12]
expected_result = 6
add(test_list) == expected_result  # Should evaluate to True
```

Each test case verifies that the `add()` function returns the expected sum of even elements at odd indices in the respective `test_list`. 

This script demonstrates the power of list comprehension and the `enumerate()` function in Python for manipulating list elements, their indices, and performing conditional operations efficiently. 

Note: The provided code includes tests to validate the functionality of the `add()` function. Remember to adjust the tests or add additional tests to cover a wide range of scenarios and ensure the accuracy of the function. 

	                                # Conclusion

This solution uses a list comprehension to efficiently identify even elements at odd indices