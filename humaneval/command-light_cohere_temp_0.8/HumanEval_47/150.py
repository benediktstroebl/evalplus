```python
def median(l: list):
    """Return median of elements in the list l.
    if len(l) % 2 == 1:
        return (l[len(l) // 2][0] + l[len(l) // 2][1]) / 2
    else:
        return l[(len(l) - 1) // 2][0]

def test_median():
    """Function to test the median function"""
    assert median([3, 1, 2, 4, 5]) == 3.0
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
    ```

def main():
    """Driver function to run the tests of the median function"""
    test_median()

if __name__ == "__main__":
    main()
```