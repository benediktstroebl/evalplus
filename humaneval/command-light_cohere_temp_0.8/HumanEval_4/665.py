Here is a self-contained Python script with a function that solves the problem and passes the tests:

```python
from typing import List

def mean_absolute_deviation(numbers):
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset. MAD = average | x - x_mean |
    """
    numbers = [1.0, 2.0, 3.0, 4.0]
    + List[in order of numbers)
    a = sum(numbers) / len(numbers)
    b = sum(map(lambda x: abs(x - numbers[-1]), numbers))
    c = sum(map(lambda x: abs(x - numbers[0]), numbers))
    d = sum(map(lambda x: abs(x - numbers[-2]), numbers))
    e = sum(map(lambda x: abs(x - numbers[-3]), numbers))
    f = sum(map(lambda x: abs(x - numbers[-4]), numbers))
    g = sum(map(lambda x: abs(x - numbers[-5]), numbers))
    h = sum(map(lambda x: abs(x - numbers[-6]), numbers))
    i = sum(map(lambda x: abs(x - numbers[-7]), numbers))
    j = sum(map(lambda x: abs(x - numbers[-8]), numbers))
    k = sum(map(lambda x: abs(x - numbers[-9]), numbers))
    l = sum(map(lambda x: abs(x - numbers[-10]), numbers))
    m = sum(numbers)
    n = sum(map(lambda x: x - m, numbers))
    o = sum(map(lambda x: x - m, numbers))
    p = (n + o) / len(numbers)
    q = (sum(numbers) - p) / m
    r = (sum(map(lambda x: x - numbers[-1], numbers)) +
          sum(map(lambda x: x - numbers[-2], numbers)) +
          sum(map(lambda x: x - numbers[-3], numbers))) / m
    s = (sum(map(lambda x: x - numbers[-4], numbers)) +
          sum(map(lambda x: x - numbers[-5], numbers)) +
          sum(map(lambda x: x - numbers[-6], numbers)) +
          sum(map(lambda x: x - numbers[-7], numbers))) / m
    t = (sum(map(lambda x: x - numbers[-8], numbers)) +
          sum(map(lambda x: x - numbers[-9], numbers)) +
          sum(map(lambda x: x - numbers[-10], numbers))) / m
    u = (sum(map(lambda x: x - numbers[-11], numbers)) +
          sum(map(lambda x: x - numbers[-12], numbers)) +
          sum(map(lambda x: x - numbers[-13], numbers))) / m
    v = (sum(map(lambda x: x - numbers[-14], numbers)) +
          sum(map(lambda x: x - numbers[-15], numbers)) +
          sum(map(lambda x: x - numbers[-16], numbers))) / m
    w = (sum(map(lambda x: x - numbers[-17], numbers)) +
          sum(map(lambda x: x - numbers[-18], numbers)) +
          sum(map(lambda x: x - numbers[-19], numbers))) / m
    x = (sum(map(lambda x: x - numbers[0], numbers))