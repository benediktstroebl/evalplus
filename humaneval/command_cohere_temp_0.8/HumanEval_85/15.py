```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function called 'add()' that takes a list of numbers as input. It aims to accumulate and return the sum of even numbers present at odd indices in the list. To achieve this, it uses a list comprehension that iterates through each element of the input list. If the index of the element is odd and the element itself is even, it adds the element to the 'even_odd' list. Finally, the function returns the sum of the elements in the 'even_odd' list, resulting in the desired sum of even numbers at odd indices. 

Here is a test case that verifies the correct operation of the `add` function:
```python
test_case = [4, 2, 6, 7]
expected_result = 2
actual_result = add(test_case)
assert actual_result == expected_result
``` 
This tests the function with the example case provided in the original problem, verifying that the function returns the expected result.