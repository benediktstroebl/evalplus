```python
def string_sequence(n: int) -> str:
    return f" {0:>{n}}"
    # 0:# N must be a positive integer
    assert isinstance(n, int) and n > 0, "Input must be a positive integer!"
    return " ".join(map(lambda x: str(x), range(n)))
    # Return the required string
    return " ".join(map(lambda x: x, range(n)))

# Example usage
n = 5
result = string_sequence(n)
print(result)  # Output: 0 1 2 3 4 5
```