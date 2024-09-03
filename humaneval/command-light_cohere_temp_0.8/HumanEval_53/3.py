```python
def add(x, y): 
    return x + y

for i in range(0,4):
    assert add(i, i+1) == i+2 

print("Success!")
```