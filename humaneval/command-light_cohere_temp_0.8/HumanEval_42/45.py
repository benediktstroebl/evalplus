```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    for i in range(n): l[i] = l[i] + 1
    return l

# Test cases
tests = [
    ("input", incr_list, [1, 2, 3])
  , ("pop", incr_list, [1, 2, 3])
  , ("str", incr_list, ["list with increment"] )
  , ("append", incr_list, [1, 2, 3])
  , ("sort", incr_list, [1, 2, 3])
  , ("repeat", incr_list, [1, 2, 3, repeat=2])
  , ("len", incr_list, [1, 2, 3, 4])
  , ("sum", incr_list, [1, 2, 3, 4])
  , ("list.copy", incr_list, [1, 2, 3])
  , ("__add__", incr_list, [1, 2, 3])
]

# Main program
def main():
    for case in tests:
        print(case[1](case[2]))

if __name__ == "__main__":
    main()
``` 
This script defines a function `incr_list` that returns a list with elements incremented by 1, and tests it against various input/output scenarios.