```markdown
### Unique Elements in a List
#### Code
```python
def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

### Example Usage
if __name__ == "__main__":
    print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```
#### Explanation
The function `unique` uses the built-in Python data structure `set`, which automatically removes duplicates. It then converts the set back to a list and sorts it using the `sorted` function. This approach ensures that the returned list is sorted in ascending order.

### Output
```
[0, 2, 3, 5, 9, 123]
```
### Running the Code
To run the code, save it in a file with a `.py` extension (e.g., `unique.py`) and execute it using Python (e.g., `python unique.py`).