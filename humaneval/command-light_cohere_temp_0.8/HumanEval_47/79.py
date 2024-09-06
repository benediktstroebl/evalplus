```python
def median(lst):
    """Return median of elements in the list lst."""
    return (lst[-1] + lst[0] + (lst[1] + lst[3]) / 4)  # O(n^1)
# Test cases
    assert median([3, 1, 2, 4, 5]) == 3.0
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
    assert median([]) == 0.0
    def main():
        return median([])  # For standalone execution
    if __name__ == "__main__":
        main()
```