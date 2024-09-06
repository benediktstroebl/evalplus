```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function named 'add', which takes a list of integers as input. It aims to collect the even integers present at odd indices within the list and then calculate their sum. To achieve this, it employs a list comprehension, iterating through each element and index of the input list. If the index is odd and the element is even, it adds the element to the 'even_odd' list. The function then returns the sum of the collected even integers, providing a convenient way to obtain the desired result. 

Here is a test case that verifies the correct operation of the provided function:
```python
def test_add():
    # Input: [4, 2, 6, 7]
    assert add([4, 2, 6, 7]) == 2 

test_add()
```
Output: