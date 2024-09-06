```python
def unique_digits(xs):
    result = [x for x in xs if not any(int(y) % 2 == 0 for y in str(x))]
    return sorted(result)
```
This Python script defines a function `unique_digits` that solves the problem as outlined in the prompt. It takes a list of positive integers, `xs`, as input and returns a sorted list of all elements that do not contain any even digits. The function filters the input list using a list comprehension that checks if none of the digits in each element's representation as a string are divisible by 2. The returned list is then sorted in increasing order, as specified in the note in the prompt. 

Here is an example of how to use this function:
```python
>>> unique_digits([15, 33, 1422, 1])
[1, 15, 33]
>>> unique_digits([152, 323, 1422, 10])
[]
```
This example test validates the function's behavior as described in the problem statement, correctly identifying the unique digits as sorted. 
To further test the function's correctness, you can also include edge cases, such as input lists containing one or more elements with only even digits, to ensure that those elements are correctly filtered out. 

The function is self-contained and does not rely on any external variables or modules, making it easy to reuse in other scripts and environments.