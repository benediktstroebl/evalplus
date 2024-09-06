```python
def unique_digits(xs):
    return sorted([x for x in xs if not any(int(y) % 2 == 0 for y in str(x))])
```
This function `unique_digits(xs)` takes a list of positive integers, `xs`, as an input and returns a sorted list of all elements that do not have any even digits. This is done using a list comprehension that iterates over each element in the input list, `xs`, and checks if any digit in each integer is even. 

The logic for checking if any digit is even in the integer `x` is done via a generator expression, `int(y) % 2 == 0 for y in str(x)`. This generates all the digits in the string representation of the integer `x`, converts them to integers to check if they are even, and thus determines whether `x` has any even digits. 

The function returns a sorted list of such elements. Thus, the output is a sorted list of elements that do not contain any even digits. 

This solution is efficient since it uses integer compression to check for the presence of even digits, which has a linear time complexity. 

The code is concise and easy to understand, making it maintainable and scalable with minimal code.