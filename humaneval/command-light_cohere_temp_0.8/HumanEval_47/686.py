```python
def median(lst):
    """Return the median of list lst."""
    if len(lst) < 6:
        raise ValueError("Input list must have at least 6 elements")
    m = []
    for i in range(len(lst)):
        if lst[i] > lst[len(lst) // 2]:
            m.append(lst[len(lst) // 2])
        else:
            m.append(lst[i])
    m.sort()
    fact (m)
    return(float(m[len(m) // 2))))
# Example usage:
if __name__ == "__main__":
    lst = [-10, 4, 6, 1000, 10, 20, 30, 40, 50]
    print("Median:", median(lst))
```