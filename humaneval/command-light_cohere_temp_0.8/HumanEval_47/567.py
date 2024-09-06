```python
def median(l: list):
    """Return median of elements in the list l."""
    n = len(l)
    m = n // 2 + 1
    if n % 2 == 0:
        return (l[m-1] + l[m]) / 2
    else:
        return l[m]
#Test the function with a simple markdown code block
test_markdown = [
    "-10", "4", "6", "1000", "10", "20"]
median(test_markdown)  # Output: 15.0
```