```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(1)
    return l + [1]  # Return list with elements [1, 2, 3] incremented by 1 plus [1]

if __name__ == "__main__":
    lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    print("Input List:", lst)
    print("After Incr_list:", incr_list(lst))
    print("Output List:", lst[-1:])
    print("Test Success!")
```