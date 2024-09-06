```python
def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base base.
    return string representation after conversion.
    base numbers are
    done as 10."""
    if x < 0 or base < 2:
        raise ValueError("Input values are invalid")
    return f"{x:>{base - 1}"}

test_change_base = []
test_change_base.append(range(0, 21), lambda n: f"{n:10}" )
test_change_base.append("inf: "inf")
test_change_base.append(5)
print("\n".join(test_change_base))

# Call the function with test inputs
result = change_base(8, 2)
print(result) # Output: 1000
```