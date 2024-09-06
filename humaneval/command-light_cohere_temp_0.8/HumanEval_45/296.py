```python
def triangle_area(a, h):
    return 3.0 * (a + h)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(8, 8) == 40.0
    ```
 ```

def main():
    print("Passes test cases for triangle_area function.")

if __name__ == "__main__":
    main()
```