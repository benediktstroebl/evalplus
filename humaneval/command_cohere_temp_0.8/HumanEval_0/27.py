```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    return any(abs(x - y) < threshold for x, y in zip(numbers, numbers[1:]))
```

This function takes a list of numbers and a threshold as parameters, it uses the `any` function with a lambda function to check for each pair of numbers in the list, whether they are closer than the threshold, and returns `True` if any of the pairs is closer than the threshold. 

To test this function, you can use the following:
```python
test_has_close_elements = '''
[] ==> False
[1.0, 2.0, 3.0] ==> False
[1.0, 2.8, 3.0, 4.0, 5.0, 2.0] ==> True
[1.0, 1.0, 3.0, 4.0, 5.0] ==> False
'''

for test in test_has_close_elements.split():
    assert eval(test) == has_close_elements(eval(test), 0.3)
```