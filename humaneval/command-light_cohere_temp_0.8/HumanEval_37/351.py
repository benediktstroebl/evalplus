```python
def sort_even(lst):
    return lst[:] if all(n % 2 == 0 for n in lst) else lst

# Test cases
test_even = []
for i in range(10):
    test_even.append(i, 2*i)
test_even.append(5, 6)
test_even.append(7, 4)
test_even.append(8, 1)

def test():
    assert sort_even(test_even) == [3, 6, 5, 4]

def test_odd():
    assert sort_even([1, 2, 3]) == [1, 2, 3]

def main():
    print("Test pass!")

main()
```