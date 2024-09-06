```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (l(lst)[n//2 - 1] + lst[n//2]) / 2
    else:
        return lst[n//2]

def l(lst):
    return sorted(lst)[len(lst)//2 - 1]

if __name__ == "__main__":
    print(median([-10, 4, 6, 1000, 10, 20])))
    print(median([3, 1, 2, 4, 5]))
```