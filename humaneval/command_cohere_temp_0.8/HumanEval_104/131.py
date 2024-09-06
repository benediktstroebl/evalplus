```python
def unique_digits(xs):
    return sorted([x for x in xs if not any(int(y) % 2 == 0 for y in str(x))])
```
This function `unique_digits(xs)` takes a list of positive integers, `xs`, as input and returns a sorted list of all elements that do not have any even digits. The function uses a list comprehension to iterate through each element `x` in the input list `xs`, checking if any digit in the string representation of `x` is even. The list comprehension constructs a new list with only the elements from the input list `xs` that don't have any even digits, and then the result is sorted in increasing order. 

Let's put this code to the test with the provided examples:
```python
tested = [
    (unique_digits([15, 33, 1422, 1]), [1, 15, 33]),
    (unique_digits([152, 323, 1422, 10]), []),
]
for case in tested:
    assert case[0] == case[1]
```
The tests successfully validate the solution against the problem statements. 
This function effectively handles the task of identifying positive integers with no even digits and can be directly used in other scripts that need this functionality. In the test block, we create a list `tested` where each element is a tuple. The first element in the tuple is the output of the function, and the second element is the expected output. The `assert` statement checks if the two elements in a tuple are equal, giving us confidence in the correctness of the function.