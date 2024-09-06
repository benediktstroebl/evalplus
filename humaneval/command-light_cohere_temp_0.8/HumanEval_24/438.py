```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest number which divides n exactly without a remainder.
    For the native implementation in C++ or other languages, this is not possible, 
    so we use the floor division trick.
    """
    int div = n // floor(n/divisor)
    return div
def test_largest_divisor(test_cases):
    assert largest_divisor(test_cases) == test_cases
# ```