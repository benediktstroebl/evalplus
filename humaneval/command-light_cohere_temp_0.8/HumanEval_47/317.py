```python
def median(lst):
    n = len(lst)
    if n % 2 == 1:
        return (l[(n-1)//2] + l[n//2]) / 2
    else:
        return l[n//2]
# Example usage:
if __name__ == "__main__":
    lst = [-10, 4, 6, 1000, 10, 20]
    print(median(lst))
```