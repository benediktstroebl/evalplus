```python
def median(l: list):
    n = len(l)
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]

# test
def test_median():
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0

test_median()
``` 
This Python script defines a function `median` that computes the median of a list's elements. It uses an simple formula to calculate the median: (middle element + second last element) / 2, which is implemented by selecting the middle element and the element directly after it. 

The `test_median` function contains a test that checks the correctness of the `median` function with a sample list.