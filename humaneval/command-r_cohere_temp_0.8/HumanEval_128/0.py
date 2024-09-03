```python
def prod_signs(arr):
    """
    Calculate the sum of magnitudes multiplied by the product of signs.

    Args:
        arr (list): A list of integers.

    Returns:
        int or float or None: Sum of magnitudes with the product of signs, or None for an empty array.
    """
    signs = [1 if a != 0 else 0 for a in arr]
    magnitudes = [abs(a) for a in arr]

    if not signs:  # Empty array
        return None

    prod = 1
    for s in signs:
        prod *= s

    return prod * sum(magnitudes)
```