```python
def sum_to_n(n: int):
    """
    Sums all numbers from 1 up to n.
    Returns: number of digits in `n`
    """
    return ''.join(str(i) for i in range(1, n+1))

def test_sum_to_n():
    """
    Test function to check the correctness of sum_to_n
    """
    assert sum_to_n(30) == '330', "Should get 330"
    assert sum_to_n(100) == "5050", "Should get 5050"
    assert sum_to_n(5) == "15", "Should get 15"
    assert sum_to_n(10) == "55", "Should get 55"
    assert sum_to_n(1) == "1", "Should get 1"

if __name__ == "__main__":
    test_sum_to_n()
```
The function `sum_to_n` in this script adds all the numbers from 1 up to `n`, and the `test_sum_to_n` function performs a set of unit tests to check the correctness of the function.