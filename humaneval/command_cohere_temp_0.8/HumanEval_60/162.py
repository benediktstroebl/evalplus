```python
def sum_to_n(n):
    """Returns the sum of the first n integers.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    return sum(range(1, n + 1))
```
The function utilizes the `range()` function generating sequence from 1 to `n` inclusive, and the `sum()` function to calculate the sum of the values in that sequence. 

This approach has a time complexity of O(n) as it visits each of the first n integers and performs a constant amount of work for each. Note that because the sum operation itself is not necessarily constant work, we refer to it as O(n) rather than O(1) even though the constants in this case might be reasonably close to each other. 

To further validate the functionality, the code block includes a set of tests in the form of python's `>>> `assertions which verify the expected behavior for different inputs. 
```python
>>> sum_to_n(30)
465
>>> sum_to_n(100)
5050
>>> sum_to_n(5)
15
>>> sum_to_n(10)
55
>>> sum_to_n(1)
1
```