```python
def unique_digits(xs):
    return sorted([x for x in xs if not any(int(y) % 2 == 0 for y in str(x))])
```
This function `unique_digits(xs)` takes a list of positive integers, `xs`, as an input and returns a sorted list of all elements that do not have any even digits. The function uses a list comprehension to iterate through each element `x` in the input list `xs`, checking if any digit in the string representation of `x` is even. 

Here is an example usage of the function implementing the given example:
```python
>> unique_digits([15, 33, 1422, 1])
[1, 15, 33]
```
And here is another example implementing the second given example:
```python
>> unique_digits([152, 323, 1422, 10])
[]
```
The function passes both test cases as expected, the first resulting in a list of elements with only digit 1, and 15, and 33, and the second resulting in an empty list as all elements in the input list have at least one even digit. 

This code provides a clean and efficient implementation in Python to solve the problem.