```python
def sum_to_n(n: int):
    """
    Returns the sum of numbers from 1 up to n.
    """
    sum(range(1, n+1))

def test_sum_to_n():
    """
    Test the sum_to_n function
    """
    assert sum_to_n(30) == 465
    assert sum_to_n(100) == 5050
    assert sum_to_n(5) == 15
    assert sum_to_n(10) == 55
    assert sum_to_n(1) == 1
    assert sum_to_n(30) + sum_to_n(100) == 1065
    assert sum_to_n(30) == 30
    assert sum_to_n(0) == 0
    assert sum_to_n(-1) == -1
    assert sum_to_n(9999) == 9999

    print("All tests passed!")

# Example usage
if __name__ == "__main__":
    test_sum_to_n()
```

This code defines the `sum_to_n` function, which calculates the sum of numbers from 1 up to a given number. The `test_sum_to_n` function contains various assertions to test the correctness of the `sum_to_n` function. The code also includes an demonstration of function usage with an example test case.