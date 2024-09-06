```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each element in the input list `l` and compare each element with the threshold value `t`. 

Here is an example of how to use the function:
```python
print(below_threshold([1, 2, 4, 10], 100))
print(below_threshold([1, 20, 4, 10], 5))
```
This would result in the following output:
```bash
True
False
```
This demonstrates that the function correctly returns whether or not all elements in the list are below the threshold value. 

This code solves the problem using a concise one-liner. It takes a list of numbers `l` and a threshold value `t` as input and returns `True` if all numbers in the list are below the threshold, and `False` otherwise. The behavior of the function is demonstrated by the provided tests, which it passes. It is important to note that the function assumes that the threshold value is a comparator and not a numeric value meant to be included in the list for comparison.