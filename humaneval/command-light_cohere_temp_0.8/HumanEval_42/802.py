```python
def incr_list(lst):
    lst[0] = 1
    return lst

# Test case 1
def test1():
    assert incr_list([1, 2, 3]) == [2, 3, 4]  # True

# Test case 2
def test2():
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 4, 10, 1, 124]  # True

def main():
    print("Test case 1 passed!")
    print("Test case 2 passed!")

if __name__ == "__main__":
    main()
```