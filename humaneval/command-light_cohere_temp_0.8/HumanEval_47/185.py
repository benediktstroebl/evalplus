```python
def median(l: list):
    """Return median of elements in the list l."""
    return(len(l)==1 and l[0] or
          (len(l)==2 and (l[0] + l[1])/2 or
             median([l[::i for i in range(len(l)-1) ]))))
#Uncommented test cases
def test1(): return median([3, 1, 2, 4, 5]) == 3
def test2(): return median([-10, 4, 6, 1000, 10, 20]) == 15
def test3(): return median([2, 2, 2]) == 2
def test4(): return median([1, 2, 4, 5, 6]) != median([2, 2, 2, 2, 2])
def test5(): return median([10, 20, 30, 40, 30]) == 30
```