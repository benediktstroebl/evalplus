Here's a Python script that includes a function to solve the given problem:
```python
def solve(n):
    """
    :param n: Integer to be converted to binary sum of digits
    :return: Binary string of the sum of its digits.
    """
    total_sum = sum(map(int, str(n)))
    return format(total_sum, 'b')
```
This script defines a function `solve(n)` that takes an integer `n` as input and calculates the sum of its digits. It converts the input integer to a string, casts the digits to integers, and calculates their sum. Finally, it uses the `format` function to convert the total sum to a binary string and returns the result. 

To follow the problem statement, the function includes a docstring that describes the function, the input, and the output. 
To test the function, you can run the following code: 
```python 
test = [
    (1000, "1"),
    (150, "110"),
    (147, "1100")
]

for n, expected in test:
    print(f"N = {n}")
    print(f"Expected = {expected}")
    print(f"Result = {solve(n)}")
    print("-----------------------")
```
This will help you verify the behavior of the function against the expected outputs. A well-written unit test is another effective way of encapsulating test cases and assuring function behavior over time, especially as the codebase evolves. This can be a simple approach using Python's built-in `unittest` module or a more feature-rich test framework like `pytest`.

Please note that this function assumes that the input `n` is a positive integer represented as a Python integer. Also, while the provided solution is efficient for this particular problem, there are other effective approaches to handling digit sums, depending on the specific constraints and context of the problem. 
The function should handle all input within the specified range of 0 to 10,000. If you encounter issues with this solution, consider addressing them by refining the input validation, which helps handle edge cases and provides more robust code. 
Please let me know if you would like to take a closer look at any of these alternative solutions or understand any part of the problem statement in more detail. I'm happy to elaborate on the concepts of efficient algorithms and binary arithmetic as they relate to this problem, as well as assist with any other topic that you wish to explore further.