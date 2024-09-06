```python
def triangle_area(a, h):
    return 3.14159 * (a**h)

if __name__ == "__main__":
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 6) == 62.5
    assert triangle_area(13, 10) == 648.0
    
    print("All functions pass their tests!")
```