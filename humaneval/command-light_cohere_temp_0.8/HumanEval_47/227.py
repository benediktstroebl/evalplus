```python
def median(l: list):
    """Return median of elements in the list l."""
    assert len(l)==len(set(l)), "Input list has different lengths!"
    assert l[-1]%2==0, "Last element does not divide the list into two almost equal parts."
    return (l[len(l)//2] + l[(len(l)//2)-1])/2
```