```python
def median(l: list):
    """Return median of elements in the list l"""
    m = l[len(l) // 2]
    if len(l) % 2 == 0:
        return (m + l[len(l) // 2]) / 2.0
   
   
    other wise:
        return m

def test_median():
    try:
        list1 = [10, 20, 30, 1, 2, 3]
        list2 = [1000, 4, 6, -10, 8, 9]
        list3 = [1, 2, 3, 4, 5, 6]
        print("For list 1", median(list1))  # Output: 2.0
        print("For list 2", median(list2))  # Output: 5.0
        print("For list 3", median(list3))  # Output: 5.0
        raise System.Error
```

test_median()