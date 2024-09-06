```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            num **= 2
        elif i % 4 == 0 and i % 3 != 0:
            num **= 3
        result += num
    return result
```
This function takes as input a list of integers, squares each element if its index is a multiple of 3, and cubes each element if its index is a multiple of 4 but not a multiple of 3. It then sums up all the modified elements and returns the result. 

To verify the functionality, you can run the following tests:
```python
test_sum_squares_output = [
    ([1, 2, 3], 6),
    ([-1, -5, 2, -1, -5], -126),
    ([], 0)
]

for lst, expected in test_sum_squares_output:
    assert sum_squares(lst) == expected
```
This script uses the `assert` statement to verify that the output of the `sum_squares` function matches the expected result for a variety of input lists. 
If the condition evaluates to False, the program will raise an AssertionError, indicating that the tested condition failed to hold true. 

This allows you to validate that the function behaves as expected, providing confidence in its correctness. 
The test suite will serve as a living documentation of the function, making it easier to understand its behavior and making it simpler to catch potential regressions in the future. It allows anyone who looks at the code to quickly understand how it is intended to work, and provides a safety net to catch errors in the code without having to manually test every possible input. 

You can add more tests to this list to cover more case scenarios in the future, which will help increase the reliability of the function and decrease the chance of bugs. 
This is a key concept in test-driven development, where each new test you add helps drive the development of the functionality, with the goal of ensuring a robust and flexible codebase. 
This development approach is especially beneficial in the early stages of producing a function, as it allows developers to optimize for flexibility and scalability from the design phase. Frequent testing also ensures the function's behavior aligns with the intended purpose and helps monitor any creeping functionality over time. 
Overall, this approach leads to cleaner, more reliable, and more resilient code. 
The Python interpreter runs these tests automatically when the module is loaded, and reports on any assertions that fail, making debugging easy for developers. 
This reduces the need for manual testing, which can be error-prone and time-consuming, increasing productivity and streamlining the development process. In this case, the Python interpreter will report a successful pass of all tests when the sum_squares function works correctly. 
This type of automated testing is a major advantage in producing robust and dependable software.