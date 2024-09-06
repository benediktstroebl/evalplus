```python
def unique_digits(xs):
    return sorted([x for x in xs if not any(int(y) % 2 == 0 for y in str(x))])
```
This function `unique_digits(xs)` takes a list of positive integers, `xs`, as an argument. It returns a sorted list of all elements that do not have any even digits. The `not any()` function is used to check if there are any digits that are even in the string representation of each number. The `sorted()` function ensures the returned list is sorted in increasing order.

Here is an example usage of the function with a similar input as provided in the problem:
```python
>>> unique_digits([15, 33, 1422, 1])
[1, 15, 33]
>>> unique_digits([152, 323, 1422, 10])
[]
```
This should return the expected output in the given markdown code block. 
If you would like to see more examples you can add more to test the function on various inputs. Haven't these examples covered the various cases? Let me know if you would like me to elaborate on any part of the script or provide additional helpful information.