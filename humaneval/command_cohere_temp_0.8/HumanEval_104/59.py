Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def unique_digits(xs):
    result = [x for x in xs if not any(int(y) % 2 == 0 for y in str(x))]
    return sorted(result)
```
The function unique_digits(xs) takes a list of positive integers xs as input and returns a sorted list of all elements that do not have any even digits. The list is sorted in increasing order. This is achieved through the use of a list comprehension, passing a generation expression as the element test through a not nested any function. A generator expression is a concise way of creating a list using the yield statement in Python. 

The script fully answers the problem statement and can be directly copied and run as a standalone Python module to test it against the given examples.