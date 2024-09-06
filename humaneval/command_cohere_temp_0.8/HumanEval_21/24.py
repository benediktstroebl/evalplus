```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [(x-min(numbers))/(max(numbers)-min(numbers))*1 for x in numbers]
```

The function `rescale_to_unit` takes a list of numbers as input and returns a list of numbers scaled to the range [0, 1] based on the smallest and largest values in the input list. This transformation is a linear transformation.

```python
def test_rescale_to_unit():
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    expected = [0.0, 0.25, 0.5, 0.75, 1.0]
    result = rescale_to_unit(numbers)
    assert result == expected
```

This test validates the functionality of the `rescale_to_unit` function by comparing the expected output with the result obtained for a specific input list.

To execute these tests, you can run the following command in your terminal:
```bash
python -m unittest your_test_file.test
```

In the command above, replace `your_test_file.test` with the path to the file that contains the test functions. This command will run the tests and provide you with a detailed report on the test results.