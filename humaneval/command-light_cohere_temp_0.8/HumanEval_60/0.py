```python
def sum_to_n(n: int):
    """Sums numbers from 1 to n"""
    return sum(range(1, n+1))

# Function Test
def test_sum_to_n():
    assert sum_to_n(30) == 465   # 30 * 11 + 5 = 465
    assert sum_to_n(100) == 5050    # 100 * 11 + 5 = 5050
    assert sum_to_n(5) == 15        # 5 * 6 + 1 = 15
    assert sum_to_n(10) == 55        # 10 * 6 + 5 = 55
    assert sum_to_n(1) == 1         # 1 * 6 + 5 = 11

# Main execution
if __name__ == "__main__":
    test_sum_to_n()
```
This code defines a function `sum_to_n` that sums numbers from 1 to the given input 'n'. It also provides a function test `test_sum_to_n` to check the correctness of the `sum_to_n` function against a set of test cases. The `main` block ensures that the function is executed only when the script is run directly, not when it's imported.