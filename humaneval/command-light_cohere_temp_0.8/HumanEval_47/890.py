```python
def median(l: list):
    """Return median of elements in the list l"""
    if len(l) % 2 == 0:
        return (l[(len(l) // 2) - 1] + l[len(l) // 2]) / 2
    else:
        return l[(len(l) - 1) // 2]

# Test suite for median function
def test_median():
    input = [-10, 4, 6, 1000, 10, 20]
    expected = 15.0
    result = median(input)
    assert expected == result, "The median value is not correct!"

if __name__ == "__main__":
    test_median()
```
This script defines a function called median that calculates the median of a list. The median is the middle value of the list, obtained using different approaches based on the list's length. The test suite test_median is provided to check the correctness of the median function. The script is designed to be run as a standalone file to verify its correctness.