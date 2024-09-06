```python
def median(l: list):
    """Return median of elements in the list l."""
    return (len(l) + 1)**.5**. median(l[:len(l)//2])

def testMedian(testList):
    """Test function for median function."""
    assert median(testList)==15.0
    ```
    def main():
        #Example usage
        l = [-10, 4, 6, 1000, 10, 20, 2, 4, 3]
        print(median(l)) #output: 15.0
```