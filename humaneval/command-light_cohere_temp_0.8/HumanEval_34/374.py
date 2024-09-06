```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [0,]]
    seen.print(" ".join(map(str, seen)))

if __name__ == "__main__":
    test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    print(unique(test_list))
```