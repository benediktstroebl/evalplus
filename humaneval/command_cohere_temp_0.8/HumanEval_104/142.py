```python
def unique_digits(xs):
    return sorted([x for x in xs if not any(int(y) % 2 == 0 for y in str(x))])
```
This function `unique_digits(xs)` takes a list of positive integers, `xs`, as an input and returns a sorted list of all elements that do not have any even digits. This is done using a list comprehension that iterates over each element in the input list `xs`, and for each element `x`, it checks if any digit in the string representation of `x` is even, using the `any()` function and a generator expression. If no even digits are found, it includes `x` in the resulting list, which is then sorted in ascending order using the `sorted()` function. 

The script will return an empty list if no elements in the input list satisfy the condition.

The function includes a note that the returned list should be sorted in increasing order, which is achieved using the `sorted()` function. This is important because it ensures that the elements are not returned in the order they are stored in the list, but rather in a coherent and predictable order.